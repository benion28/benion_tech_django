from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_area, name='practice-area'),
    path('edit-item/<str:params>', views.edit_item, name='edit-item'),
    path('delete-item/<str:params>', views.delete_item, name='delete-item'),
    path('delete-all-items', views.delete_all_item, name='delete-all-items')
]