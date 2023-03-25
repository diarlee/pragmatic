from django.forms import ModelForm

from profileApp.models import Profile

class ProfileCreatioinForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']