from django.shortcuts import render

from service.models import Service


def home(request):
    services_obj = Service.objects.all()
    context = {
        'services': services_obj}
    return render(request, 'home.html',context)

