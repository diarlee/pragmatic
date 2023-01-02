from django.views.generic import CreateView, UpdateView

from .models import Profile
from .forms import ProfileCreatioinForm

from django.urls import reverse, reverse_lazy

from django.utils.decorators import method_decorator
from .decorators import profile_ownership_required

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreatioinForm
    template_name = 'profileApp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountApp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreatioinForm
    template_name = 'profileApp/update.html'

    def get_success_url(self):
        return reverse('accountApp:detail', kwargs={'pk': self.object.user.pk})
