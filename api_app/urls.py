from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.TestArea.as_view(), name='test'),
    path('student-demo/', views.StudentApi.as_view(), name='demo-student'),
    path('token', obtain_auth_token, name='token')
]
