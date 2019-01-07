from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from authentication.views import GetUserView, LogoutView, RegisterUserView, RequestAuthEmailCodeView, LoginEmailCodeView, ActivateAccountView, LogoutSessionView

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('logout-session/', LogoutSessionView.as_view()),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('activate-account/', ActivateAccountView.as_view()),
    path('request-auth-email-code/', RequestAuthEmailCodeView.as_view()),
    path('login-auth-email/', LoginEmailCodeView.as_view()),
    path('prueba/', RegisterUserView.as_view()),
]
