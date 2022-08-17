import imp
from django.urls import path
from accountApp.views import hello_world
from .views import AccountCreateView

app_name = 'accountApp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create')
]
