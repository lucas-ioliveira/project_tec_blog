from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_name", "comment_email", "comment")

    def clean(self):
        data = self.cleaned_data
        form_name = data.get("comment_name")
        form_email = data.get("comment_email")
        form_comment = data.get("comment")

        if len(form_name) < 5:
            self.add_error("comment_name", "Nome precisa ter mais de 5 caracteres.")
