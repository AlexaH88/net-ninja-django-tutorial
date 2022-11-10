from django.contrib import admin
from django.urls import path, include
# from . means importing from the same directory this file is in
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# need to name the views import so that django doesn't get confused with same folder views as above
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # link to articles browser url to articles app urls
    path('articles/', include('articles.urls')),
    # from views file fire about function
    path('about/', views.about),
    path('', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
