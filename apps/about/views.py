from django.shortcuts import render
from apps.about.models import AboutPageSettings, AboutAdvantages
# Create your views here.

def about(request):
    about_id = AboutPageSettings.objects.latest("id")
    about_all = AboutAdvantages.objects.all()
    return render(request, 'base/about.html', locals())
