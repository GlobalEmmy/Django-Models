from pdb import post_mortem
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey("Post", on_delete=models.CASCADE)
    created_date = models.DateTimeField
    published_dated = models.DateTimeField

