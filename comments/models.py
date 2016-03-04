from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_published = models.DateTimeField(default=timezone.now())
    text = models.TextField(blank=True)