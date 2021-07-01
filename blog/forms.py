from django import forms
from django.db import models
from django.db.models import fields
from .models import Blog

class BlogForm(forms.ModelForm): #()안에 있는 건 상속받는 것
    class Meta: #이름표역할
        model = Blog
        fields = ['title', 'writer', 'body', 'image']


