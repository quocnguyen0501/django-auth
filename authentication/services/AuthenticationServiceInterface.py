class AuthenticationServiceInterface:

  def validate_user_by_email_password(self, email, password):
    pass

  def login(self, request):
    pass

  def logout(self, request):
    pass

  def sign_up(self, request):
    pass

  def login_with_google(self, request):
    pass

  def google_oauth_callback(self, request):
    pass
