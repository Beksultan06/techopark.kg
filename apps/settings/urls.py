from django.urls import path
from apps.settings.views import index, contact, testimonials

urlpatterns = [
    path("", index, name='index'), 
    path("contact/", contact, name='contact'),
    path("testimonials", testimonials, name='testimonials'),
]