from django.urls import path
from account.views import user_login
from django.contrib.auth.views import LoginView, LogoutView
from account.views import dashboard
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
]