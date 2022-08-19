from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('profile/', views.user_profile, name='profile'),
    path('setting/', views.user_setting, name='setting'),
    path('remove-profile/<str:id>', views.remove_profile, name='remove-profile'),
    path('delete-user/<str:user>', views.delete_user, name='delete-user'),
    path('edit-user/<str:params>', views.edit_user, name='edit-user'),
    path('change-password/<str:params>', views.change_password, name='change-password-user')
]