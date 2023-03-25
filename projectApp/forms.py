from django.forms import ModelForm

from projectApp.models import Project

class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']