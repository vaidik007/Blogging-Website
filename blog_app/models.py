from django.db import models

# Create your models here.
class  blog_post(models.Model):
     Post_Title = models.CharField(max_length = 200, unique=True)
     Slug = models.SlugField(max_length = 200, unique=True)
     content = models.TextField()
     created_on = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ['-created_on']

def __str__(Self):
    return self.Post_Title
