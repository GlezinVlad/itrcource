from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tagging.registry import register
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(default=timezone.now())
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)
    text_rendered = models.TextField(blank=True)
    media_url = models.CharField(max_length=200, blank=True)
    template_name = models.CharField(max_length=50, blank=True)
    ratings = GenericRelation(Rating, related_query_name='foos')

    def avg_rating(self):
        return self.ratings.all()[0].average if self.ratings.all().exists() else 0


register(Post)

