from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('profile/',views.profile,name='user-profile'),
    path('profile/update/',views.profile_update,name='user-profile-update'),
    path('logout/', views.logout_view,name='user-logout'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]




   