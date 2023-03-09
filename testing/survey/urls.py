from django.urls import path
from .views import index, start_survey, get_user_list, profile

app_name = 'survey'

urlpatterns = [
    path('', index, name='index'),
    path('test/<slug:slug>/', start_survey, name='start_survey'),
    path('users/', get_user_list, name='get_user_list'),
    path('me/', profile, name='profile'),
]
