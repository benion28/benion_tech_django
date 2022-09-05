"""benion_tech_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from . import views
from user_app import views as user_app_view
from chat_app import views as chat_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/', include('user_app.urls')),
    path('chat/', include('chat_app.urls')),
    path('practice-area/', include('practice_area.urls')),
    path('api/', include('api_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('send-message', chat_app_view.send_message, name='send-message'),
    path('get-messages', chat_app_view.GetMessages.as_view(), name='get-messages'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('add-user', views.add_user, name='add-user'),
    path('contact', views.contact, name='contact'),
    path('resume', views.resume, name='resume'),
    path('posts', views.all_posts, name='all-posts'),
    path('posts/category/<str:params>', views.category_posts, name='category-posts'),
    path('posts/tag/<str:params>', views.tag_posts, name='tag-posts'),
    path('posts/tag/', views.tag_search, name='tag-search'),
    path('post/<str:params>', views.single_post, name='single-post'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/details/<str:params>', views.portfolio_details, name='portfolio-details'),
    path('about', views.about, name='about'),
    path('need-help', views.need_help, name='need-help'),
    path('coming-soon', views.coming_soon, name='coming-soon'),
    path('users/users-table/', user_app_view.users_table, name='users'),
    path('users/cbt-users-table/', user_app_view.cbt_users_table, name='cbt-users-tables'),
    path('benion-tech-server/cbt-users/', user_app_view.cbt_users, name='cbt-users'),
    path('benion-tech-server/exams/', user_app_view.exams, name='exams'),
    path('benion-tech-server/scores/', user_app_view.scores, name='scores'),
    path('benion-tech-server/messages/', user_app_view.messages, name='messages'),
    path('benion-tech-server/images/', user_app_view.images, name='images'),
    path('benion-tech-server/posts/', user_app_view.posts, name='posts'),
    path('users/exams-table/', user_app_view.exams_table, name='exams-table'),
    path('users/scores-table/', user_app_view.scores_table, name='scores-table'),
    path('users/messages-table/', user_app_view.messages_table, name='messages-table')
]

handler404 = views.not_found
handler500 = views.server_error