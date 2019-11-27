from django.db import models

# Create your models here.
class Post(models.Model):
    """
    A simple Post class for Blog App.
    """

    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title