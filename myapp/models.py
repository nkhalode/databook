from django.db import models

# Create your models here.
class BlogApp(models.Model):
    title=models.CharField(max_length=70)
    desc=models.TextField()
    author=models.CharField(max_length=70)

    def __str__(self):
        return self.title
    




