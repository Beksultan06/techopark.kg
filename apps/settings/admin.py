from django.contrib import admin
from apps.settings.models import BaseBanner, Settings, Services, Statistic, News, Contact

admin.site.register(BaseBanner)
admin.site.register(Settings)
admin.site.register(Services)
admin.site.register(Statistic)
admin.site.register(News)
admin.site.register(Contact)