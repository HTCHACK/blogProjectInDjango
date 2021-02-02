from django.forms import fields, models
from django import forms
from .models import Contact, Subscribe, BlogComment

#choices = [('liverpool','liverpool'), ('spurs','spurs'), ('premier','premier'),]

class ContactForm(models.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SubscribeForm(models.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = BlogComment 
        fields = ('name', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


