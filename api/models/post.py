from django.db import models
from .user import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    publish_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
