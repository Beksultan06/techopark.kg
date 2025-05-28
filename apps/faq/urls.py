from apps.faq.views import faq_view
from django.urls import path

urlpatterns = [
    path("faq", faq_view, name='faq')
]
