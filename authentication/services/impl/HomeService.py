from django.shortcuts import render, redirect

from authentication.services.HomeServiceInterface import HomeServiceInterface


class HomeService(HomeServiceInterface):
  def home(self, request):
    user_id = request.session.get('user_id')
    email = request.session.get('email')
    name = request.session.get('name')

    if not user_id:
      if not request.path.startswith('/auth'):
        return redirect('/auth/login')

    return render(request, 'success.html',
                  {'username': name, 'email': email})
