from django.db import models

# Create your models here.

# inherit basic functionality with the class Model from django's models method 
class Article(models.Model):
    title = models.CharField(max_length=100)
    # slug is url address of article
    slug = models.SlugField()
    body = models.TextField()
    # time and date is automatically added thanks to parameter
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later    
