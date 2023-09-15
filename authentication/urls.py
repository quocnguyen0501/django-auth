from django.urls import path
from authentication.views.AuthenticationView import AuthenticationView
from authentication.views.HomeView import HomeView


urlpatterns = [
    path('', HomeView.as_view({'get': 'home'}),
         name='home'),
    path('login', AuthenticationView.as_view({'get': 'login', 'post': 'login'}),
         name='login'),
    path('logout', AuthenticationView.as_view({'get': 'logout'}),
         name='logout'),
    path('register', AuthenticationView.as_view({'get': 'sign_up', 'post': 'sign_up'}),
         name='sign_up'),
    path('login_with_google/', AuthenticationView.as_view({'get': 'login_with_google'}),
         name='login_with_google'),
    path('accounts/google/login/callback/', AuthenticationView.as_view({'get': 'google_oauth_callback'}),
         name='google_oauth_callback')
]
