from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='passwordChange'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='passwordChangeDone'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]