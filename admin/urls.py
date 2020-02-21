from django.urls import path, include
from . import views

urlpatterns = [
     path('', include('admin.login.urls')),
     path('dashboard/', include('admin.dashboard.urls')),
     path('genre/', include('admin.genre.urls')),
     path('mood/', include('admin.mood.urls')),
     path('artist/', include('admin.artist.urls')),
     path('song/', include('admin.song.urls')),
     # path('users/', include('admin.user.urls')),
]