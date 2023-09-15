from rest_framework import viewsets

from authentication.services.impl.AuthenticationService import AuthenticationService


class AuthenticationView(viewsets.ViewSet):

  def __init__(self, *args, **kwargs):
    self.authentication_service = AuthenticationService()
    super().__init__(*args, **kwargs)

  def login(self, request):
    return self.authentication_service.login(request=request)

  def logout(self, request):
    return self.authentication_service.logout(request=request)

  def sign_up(self, request):
    return self.authentication_service.sign_up(request=request)

  def login_with_google(self, request):
    return self.authentication_service.login_with_google(request=request)

  def google_oauth_callback(self, request):
    return self.authentication_service.google_oauth_callback(request=request)
