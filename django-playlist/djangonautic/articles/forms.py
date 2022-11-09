from django import forms
from . import models


# create unique class using ModelForm from django forms
class CreateArticle(forms.ModelForm):
    # which fields do we want to be present
    # and from which model do we want to inherit these from
    class Meta:
        # use Article model we created in models.py
        model = models.Article
        # select which fields we want
        # date is automatically added
        fields = ['title', 'body', 'slug', 'thumb']
