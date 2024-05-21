from django.shortcuts import render

# Create your views here.
def services(request):
    context = {
        'services': 'active'
    }
    return render(request, 'serv/service.html', context)