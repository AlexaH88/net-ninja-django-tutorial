from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# import forms.py file
from . import forms


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
    if request.method == 'POST':
        # request.FILES is required for file uploads
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            # save article to variable instance, and don't commit save yet to db
            instance = form.save(commit=False)
            # attach author to instance and make it equal to the logged in user via request
            instance.author = request.user
            # save instance, with author attached
            instance.save()
            return redirect('articles:list')
    else:
        # create new instance of our CreateArticle form
        form = forms.CreateArticle()
    # include form as third parameter, to be viewed by user
    return render(request, 'articles/article_create.html', {'form': form})
