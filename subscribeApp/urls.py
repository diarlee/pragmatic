from django.urls import path

from subscribeApp.views import SubsriptionView, SubscriptioinListView

app_name = 'subscribeApp'

urlpatterns = [
    path('subscribe/', SubsriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptioinListView.as_view(), name='list')
]