
from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_world(request):

    if request.method == 'POST':
        return render(request, 'accountApp/hello_world.html', context={'text' : 'POST METHOD!!!'})
    else:
        return render(request, 'accountApp/hello_world.html', context={'text' : 'GET METHOD!!!'})