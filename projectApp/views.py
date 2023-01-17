from django.shortcuts import render

from django.views.generic import CreateView, DetailView, ListView
from projectApp.forms import ProjectCreateForm

from projectApp.models import Project

from django.urls import reverse

# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projectApp/create.html'

    def get_success_url(self):
        return reverse('projectApp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectApp/detail.html'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectApp/list.html'
    paginate_by = 5
