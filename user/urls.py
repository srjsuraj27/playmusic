from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='user.login'),
    path('register', views.register, name='user.register'),
    path('signup',views.signup,name='user.signup'),
    path('login/post',views.login_post,name='user.login_post'),
    path('logout',views.logout,name='user.logout'),
    path('index',views.index,name='user.index'),
]