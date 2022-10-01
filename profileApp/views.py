from django.views.generic import CreateView

from .models import Profile
from .forms import ProfileCreatioinForm

from django.urls import reverse_lazy

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreatioinForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'profileApp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid()
