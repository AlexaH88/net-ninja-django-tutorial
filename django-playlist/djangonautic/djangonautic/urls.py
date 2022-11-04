from django.contrib import admin
from django.urls import path, include
# from . means importing from the same directory this file is in
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # link to articles browser url to articles app urls
    path('articles/', include('articles.urls')),
    # from views file fire about function
    path('about/', views.about),
    path('', views.homepage),
]
