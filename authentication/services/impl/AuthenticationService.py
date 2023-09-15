from authentication.forms.RegistrationForm import RegistrationForm
from authentication.entities.User import User
from authentication.entities.UserToken import UserToken
from authentication.services.AuthenticationServiceInterface import AuthenticationServiceInterface
from random import randrange

from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from authlib.integrations.django_client import OAuth

oauth = OAuth()
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
  name='google',
  client_id='',
  client_secret='',
  authorize_params={'scope': 'openid profile email'},
  server_metadata_url=CONF_URL,
  client_kwargs={
    'scope': 'openid email profile'
  }
)


class AuthenticationService(AuthenticationServiceInterface):

  def validate_user_by_email_password(self, email, password):
    try:
      user = User.objects.get(email=email)

      return check_password(password=user.password, encoded=password)

    except User.DoesNotExist:
      return False

  def login(self, request):
    if request.session.get('user_id'):
      return redirect('/')

    if request.method == "POST":

      if(self.validate_user_by_email_password(email=request.POST.data["email"],
                                              password=request.POST.data["password"])):
        email = request.POST.data["email"]
        user = User.objects.get(email=email)
        user.status(1)

        user.save()

        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['name'] = user.name

        return render(request, 'success.html',
                      {'username': user.name, 'email': email})
      else:
        return render(request, 'login.html', {'message': 'Email or Password was wrong. Please try again'})

    return render(request, 'login.html')

  def logout(self, request):
    email = request.GET.get('email')

    user = User.objects.get(email=email)

    user.status = 1
    user.save()

    return redirect('/auth/login')

  def sign_up(self, request):
    if request.session.get('user_id'):
      return redirect('/')

    if request.method == "POST":
      form = RegistrationForm(request.POST)

      if form.is_valid():
        user_modal = User(
          email=form.cleaned_data["email"],
          password=make_password(form.cleaned_data["password"]),
          name=form.cleaned_data["name"],
          phone=form.cleaned_data["phone"]
        )

        user_modal.save()

        verify_code = str(randrange(100000, 999999))
        cache.set(user_modal.email, verify_code, timeout=3600)

        email = EmailMessage('Verify email', 'Hi ' +
                             user_modal.name +
                             ", hear is your verification code " +
                             verify_code,
                             to=[user_modal.email])
        email.send()
        return redirect('/auth/login')

    return render(request, 'register.html')

  def login_with_google(self, request):
    redirect_uri = 'http://127.0.0.1:8000/auth/accounts/google/login/callback/'
    return oauth.google.authorize_redirect(request, redirect_uri)

  def google_oauth_callback(self, request):
    if request.session.get('user_id'):
      return redirect('/')

    token = oauth.google.authorize_access_token(request)
    access_token = token['access_token']
    user_info = token['userinfo']
    email = user_info['email']
    username = user_info['name']

    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      user = User(email=email, name=username, password="", phone="")
      user.save()

    user = User.objects.get(email=email)

    request.session['user_id'] = user.id
    request.session['email'] = user.email
    request.session['name'] = user.name

    userToken = UserToken(user=user, refresh_token="", access_token=access_token)
    userToken.save()

    return render(request, 'success.html', {'username': user.name, 'email': email})
