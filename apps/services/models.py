from django.db import models

# Create your models here.
class ServicesPageSettings(models.Model):
    title_exceptional = models.CharField(max_length=155)
    description_exceptional = models.TextField()
    title_profesional = models.CharField(max_length=155)
    description_profesional = models.TextField()
    title_services = models.CharField(max_length=155)
    description_services = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title_exceptional

    class Meta:
        verbose_name_plural = 'Настройки Страницы Услуги'


class Services(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Услуги'    