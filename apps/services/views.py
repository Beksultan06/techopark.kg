from django.shortcuts import render
from apps.settings.models import Services as ServicesSettings
from apps.services.models import ServicesPageSettings, Services


def services(request):
    services_all = ServicesSettings.objects.all()
    services_id = ServicesPageSettings.objects.latest("id")
    service_all = Services.objects.all()
    return render(request, 'base/services.html', locals())