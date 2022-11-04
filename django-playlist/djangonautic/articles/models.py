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

    # defines how an article is going to look (output)
    def __str__(self):
        return self.title

    # add snippet model to show only a selection of the body text in article list view
    def snippet(self):
        # show only first 50 characters of the body string + ...
        return self.body[:50] + '...'
