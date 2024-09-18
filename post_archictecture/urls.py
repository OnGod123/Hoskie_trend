from django.urls import path
from . import views

urlpatterns = [
    path('hoskie/images/<str:username>/', views.user_images, name='user_images'),
    path('hoskie/videos/<str:username>/', views.user_videos, name='user_videos'),
    path('hoskie/blogs/<str:username>/', views.user_blogs, name='user_blogs'),
    
    path('hoskie/image/<str:username>/<int:image_id>/', views.specific_image, name='specific_image'),
    path('hoskie/video/<str:username>/<int:video_id>/', views.specific_video, name='specific_video'),
    path('hoskie/blog/<str:username>/<int:blog_id>/', views.specific_blog, name='specific_blog'),
]
