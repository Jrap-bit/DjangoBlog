from django.urls import path, re_path
from . import views


urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('counter.html', views.counter, name='counter'),
    path('Donate.html', views.donate, name='Donate'),
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
    path('logout.html', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('register', views.register, name='register')
]