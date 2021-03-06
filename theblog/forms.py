# -*- coding: utf-8 -*-

from django import forms
from .models import Post,Category 

cats = Category.objects.all().values_list('name','name')
cats_list =[]

for item in cats:
    cats_list.append(item)
    print(item)
    
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body')
        
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=cats_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')
        
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            }