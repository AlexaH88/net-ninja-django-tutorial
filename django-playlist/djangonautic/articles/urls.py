from django.urls import path
# from . means importing from the same directory this file is in
from . import views

app_name = 'articles'

urlpatterns = [
    # "homepage" of the articles/ url
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail"),
]
