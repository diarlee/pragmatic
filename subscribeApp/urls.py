from django.urls import path

from subscribeApp.views import SubsriptionView

app_name = 'subscribeApp'

urlpatterns = [
    path('subscribe/', SubsriptionView.as_view(), name='subscribe')
]