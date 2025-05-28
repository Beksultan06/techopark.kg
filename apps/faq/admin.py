from django.contrib import admin
from apps.faq.models import FAQCategory, FAQ

admin.site.register(FAQ)
admin.site.register(FAQCategory)