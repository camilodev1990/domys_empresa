from django.urls import path
from aplicaciones.core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('confirm-logout/', views.ConfirmLogoutView.as_view(), name='confirm_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password/change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
]
