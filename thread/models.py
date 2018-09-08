from django.conf import settings
from django.db import models

class Thread(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread_id=models.PositiveIntegerField(null=True, blank=True)
    parent_id=models.PositiveIntegerField(null=True, blank=True)
    image=models.FileField(null=True, blank=True)
    content = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

