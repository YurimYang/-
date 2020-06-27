from django.db import models

# Create your models here.
# makemigartions 는 sql로 바꿔주고 migrate는 적용
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(upload_to = 'post/image')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title