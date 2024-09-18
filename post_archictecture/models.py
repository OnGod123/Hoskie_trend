from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)  # Path where the image is stored

    def __str__(self):
        return f'{self.image_name} by {self.user.username}'

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=255)
    video_path = models.CharField(max_length=255)  # Path where the video is stored

    def __str__(self):
        return f'{self.video_name} by {self.user.username}'

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField()

    def __str__(self):
        return f'{self.blog_title} by {self.user.username}'
