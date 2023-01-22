from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import RedirectView

from django.urls import reverse

from django.shortcuts import get_object_or_404

from subscribeApp.models import Subscription
from projectApp.models import Project

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
            print(1)
        else:
            Subscription(user=user, project=project).save()
        
        return super(SubsriptionView, self).get(request, *args, **kwargs)