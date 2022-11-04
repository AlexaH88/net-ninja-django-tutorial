from django.urls import path
# from . means importing from the same directory this file is in
from . import views

urlpatterns = [
    # "homepage" of the articles/ url
    path('', views.article_list),
]
