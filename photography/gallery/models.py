from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/photos/')
    post = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user.username} - {self.image.name}"

