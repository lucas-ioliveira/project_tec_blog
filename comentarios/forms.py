from django import forms
from .models import Comment

# class FormComment(forms.Form):
#      nome = forms.CharField(label='Nome', max_length=100)
#      email = forms.EmailField(label='E-mail', max_length=100)
#      comentario = forms.CharField(label='comentario', widget=forms.Textarea())

class FormCommentModel(forms.ModelForm):
     comment_name = forms.CharField(label='Nome', max_length=100)
     comment_email = forms.EmailField(label='E-mail', max_length=100)
     comment = forms.CharField(label='comentario', widget=forms.Textarea())
     class Meta:
          model = Comment
          fields = ('comment_name', 'comment_email', 'comment')


