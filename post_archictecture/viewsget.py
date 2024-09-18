from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Image, Video, Blog
import json

# View to handle both GET and POST requests for images
@csrf_exempt
def user_images(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'GET':
        # Return all images for the user
        images = Image.objects.filter(user=user)
        return render(request, 'user_images.html', {'images': images, 'user': user})
    
    elif request.method == 'POST':
        # Handle POST request to create a new image
        try:
            data = json.loads(request.body)
            image_name = data.get('image_name')
            image_path = data.get('image_path')

            if not image_name or not image_path:
                return JsonResponse({"error": "Invalid data"}, status=400)

            new_image = Image.objects.create(user=user, image_name=image_name, image_path=image_path)
            return JsonResponse({"message": f"Image '{new_image.image_name}' added successfully"}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# View to handle both GET and POST requests for videos
@csrf_exempt
def user_videos(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'GET':
        # Return all videos for the user
        videos = Video.objects.filter(user=user)
        return render(request, 'user_videos.html', {'videos': videos, 'user': user})
    
    elif request.method == 'POST':
        # Handle POST request to create a new video
        try:
            data = json.loads(request.body)
            video_name = data.get('video_name')
            video_path = data.get('video_path')

            if not video_name or not video_path:
                return JsonResponse({"error": "Invalid data"}, status=400)

            new_video = Video.objects.create(user=user, video_name=video_name, video_path=video_path)
            return JsonResponse({"message": f"Video '{new_video.video_name}' added successfully"}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# View to handle both GET and POST requests for blogs
@csrf_exempt
def user_blogs(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'GET':
        # Return all blogs for the user
        blogs = Blog.objects.filter(user=user)
        return render(request, 'user_blogs.html', {'blogs': blogs, 'user': user})
    
    elif request.method == 'POST':
        # Handle POST request to create a new blog post
        try:
            data = json.loads(request.body)
            blog_title = data.get('blog_title')
            blog_content = data.get('blog_content')

            if not blog_title or not blog_content:
                return JsonResponse({"error": "Invalid data"}, status=400)

            new_blog = Blog.objects.create(user=user, blog_title=blog_title, blog_content=blog_content)
            return JsonResponse({"message": f"Blog '{new_blog.blog_title}' added successfully"}, status=201)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
