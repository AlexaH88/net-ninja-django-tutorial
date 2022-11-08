from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def article_list(request):
    # grab all the records from the Article database table and order by date
    articles = Article.objects.all().order_by('date')
    # add articles to the render properties below as a dictionary
    return render(
        request, 'articles/article_list.html', {'articles': articles}
        )


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(
        request, 'articles/article_detail.html', {'article': article}
        )


# view will only run if user is logged in
# and redirect the user to /accounts/login/ if not logged in
@login_required(login_url="/accounts/login/")
def article_create(request):
    return render(request, 'articles/article_create.html')
