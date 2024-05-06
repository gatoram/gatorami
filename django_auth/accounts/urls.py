from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
                                           PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    
    path('password-reset/',
         PasswordResetView.as_view(
              email_template_name="accounts/password_reset_email.html",
              template_name="accounts/password_reset_form.html",
              success_url =reverse_lazy("accounts:password_reset_done")),
         name='password_reset'),
    
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name='password_reset_done'), 
    
     path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
          template_name="accounts/password_reset_confirm.html",
          success_url =reverse_lazy("accounts:password_reset_complete")),
         name='password_reset_confirm'),
     
     path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name='password_reset_complete'),
]
