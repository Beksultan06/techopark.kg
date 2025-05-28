from django.shortcuts import render
from apps.faq.models import FAQ, FAQCategory
# Create your views here.

def faq_view(request):
    categories = FAQCategory.objects.prefetch_related('faqs')
    return render(request, 'base/faqs.html', {'categories': categories})