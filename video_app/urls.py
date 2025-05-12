from django.urls import path
from . import views

app_name = 'video_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
]