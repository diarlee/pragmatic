from django.shortcuts import render

from django.views.generic import CreateView, DetailView, ListView

from django.views.generic.list import MultipleObjectMixin
from articleApp.models import Article
from subscribeApp.models import Subscription

from projectApp.forms import ProjectCreateForm

from projectApp.models import Project

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse

# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projectApp/create.html'

    def get_success_url(self):
        return reverse('projectApp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectApp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                                subscription = subscription,
                                                                 **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectApp/list.html'
    paginate_by = 25
