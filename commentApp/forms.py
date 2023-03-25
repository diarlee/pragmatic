from django.forms import ModelForm

from commentApp.models import Comment

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']