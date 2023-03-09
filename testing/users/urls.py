from django.contrib.auth.views import (LogoutView, LoginView,)
from django.urls import path, reverse_lazy
from .views import SignUp

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout',
    ),

    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),

    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
]
