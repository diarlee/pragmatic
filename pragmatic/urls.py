"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from articleApp.views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accountApp.urls')),
    path('profiles/', include('profileApp.urls')),
    path('articles/', include('articleApp.urls')),
    path('comments/', include('commentApp.urls')),
    path('projects/', include('projectApp.urls')),
    path('subscribes/', include('subscribeApp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)