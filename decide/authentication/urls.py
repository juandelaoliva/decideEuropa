from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import TemplateView
from .views import GetUserView, LogoutView, RegisterUserView, RequestAuthEmailCodeView, LoginEmailCodeView


from .views import GetUserView, LogoutView, RegisterUserView, RequestAuthEmailCodeView, LoginEmailCodeView, ActivateAccountView, LogoutSessionView

urlpatterns = [
    path('login/', obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('logout/', LogoutView.as_view()),
    path('logout-session/', LogoutSessionView.as_view(), name='logout'),
    path('getuser/', GetUserView.as_view()),
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('activate-account/', ActivateAccountView.as_view()),
    path('request-auth-email-code/', RequestAuthEmailCodeView.as_view(), name='login'),
    path('login-auth-email/', LoginEmailCodeView.as_view()),
    path('prueba/', RegisterUserView.as_view()),
]
