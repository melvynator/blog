from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to="illustrations")
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = HTMLField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
