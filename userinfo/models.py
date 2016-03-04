from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime



class UserInfo(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)
    info = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    language = models.CharField(max_length=10, default='English')
    theme = models.CharField(max_length=10, default='light')
    avatar_url = models.URLField(blank=True, default='http://res.cloudinary.com/dusvendql/image/upload/v1455886667/blrym6ryw2w3n9m6qveg.png')

    def fullname(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def attrs(self):
        for field in self._meta.fields:
            if field.name != 'user':
                yield field.name, getattr(self, field.name)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_userinfo(**kwargs):
    if kwargs['instance'].date_joined > timezone.now() - datetime.timedelta(seconds=3):
        info = UserInfo(user=kwargs['instance'])
        info.first_name = kwargs['instance'].first_name
        info.last_name = kwargs['instance'].last_name
        info.email = kwargs['instance'].email
        info.save()
