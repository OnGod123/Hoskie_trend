from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Image, Video, Blog

# View to display a user's images
def user_images(request, username):
    user = get_object_or_404(User, username=username)
    images = Image.objects.filter(user=user)
    return render(request, 'user_images.html', {'images': images, 'user': user})

# View to display a user's videos
def user_videos(request, username):
    user = get_object_or_404(User, username=username)
    videos = Video.objects.filter(user=user)
    return render(request, 'user_videos.html', {'videos': videos, 'user': user})

# View to display a user's blogs
def user_blogs(request, username):
    user = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(user=user)
    return render(request, 'user_blogs.html', {'blogs': blogs, 'user': user})

# Specific image, video, or blog
def specific_image(request, username, image_id):
    user = get_object_or_404(User, username=username)
    image = get_object_or_404(Image, id=image_id, user=user)
    return render(request, 'specific_image.html', {'image': image, 'user': user})

def specific_video(request, username, video_id):
    user = get_object_or_404(User, username=username)
    video = get_object_or_404(Video, id=video_id, user=user)
    return render(request, 'specific_video.html', {'video': video, 'user': user})

def specific_blog(request, username, blog_id):
    user = get_object_or_404(User, username=username)
    blog = get_object_or_404(Blog, id=blog_id, user=user)
    return render(request, 'specific_blog.html', {'blog': blog, 'user': user})
