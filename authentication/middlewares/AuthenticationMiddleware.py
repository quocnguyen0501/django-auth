from django.shortcuts import redirect

from authentication.entities.User import User


class AuthenticationMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    user_id = request.session.get('user_id')

    if not user_id:
      if not request.path.startswith('/auth'):
        return redirect('/auth/login')
    else:
      try:
        user = User.objects.get(id=user_id)
        if user.status == 0:
          user.status = 1
          user.save()
      except User.DoesNotExist:
        del request.session['user_id']
        return redirect('/auth/login')

    return self.get_response(request)
