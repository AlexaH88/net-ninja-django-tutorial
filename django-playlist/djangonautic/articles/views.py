from django.shortcuts import render
from .models import Article


# Create your views here.
def article_list(request):
    # grab all the records from the Article database table and order by date
    articles = Article.objects.all().order_by('date')
    # add articles to the render properties below as a dictionary
    return render(
        request, 'articles/article_list.html', {'articles': articles}
        )
