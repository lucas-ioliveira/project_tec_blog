from django.db import models

# Importando módulo de contatos
from posts.models import Posts

# Importação do forms do django
from django import forms


class FormContato(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ("mostrar",)
