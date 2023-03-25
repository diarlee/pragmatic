from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import RedirectView, ListView

from django.urls import reverse

from django.shortcuts import get_object_or_404

from subscribeApp.models import Subscription
from projectApp.models import Project
from articleApp.models import Article

# Create your views here.

@method_decorator(login_required, 'get')
class SubsriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectApp:detail', kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
            print()
        else:
            Subscription(user=user, project=project).save()
        
        return super(SubsriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptioinListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeApp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list

    # def get_context_data(self, **kwargs):
    #     subscription = Subscription.objects.filter(user=self.request.user).values_list('project')
    #     return super().get_context_data(subscription = subscription, **kwargs) 

    