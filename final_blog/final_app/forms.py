from django import forms
from .models import Post, Category, Comment
# choices=[('coding', 'coding'), ('sports', 'sports'), ....] is hard coded way of adding choices
choices = Category.objects.all().values_list('name', 'name')
choice_list = [choice for choice in choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author',
                  'category', 'body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add the title tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'abcd', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add the snippet for post'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add the title tag'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add the main content for post'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add the snippet for post'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add the Comment'}),
        }
