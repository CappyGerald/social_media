from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,PasswordChangeDoneView,\
     PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from account.views import dashboard







urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ), 
    path('password-change/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/', PasswordResetConfirmView.as_view(), name='confirm_password_change'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]