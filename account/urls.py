from django.urls import path
from account.views import user_login

urlpatterns = [
    path('account/', user_login, name='login'),
]