from django.db import models

# Create your models here.

class AboutPageSettings(models.Model):
    title = models.CharField(max_length=155)
    year = models.CharField(max_length=155)
    text = models.TextField()
    image = models.ImageField(upload_to='about_page')
    title_choices_us = models.CharField(max_length=155)
    description = models.TextField()
    title_ceo = models.CharField(max_length=155)
    description_ceo = models.TextField()
    name_ceo = models.CharField(max_length=155)
    image_ceo = models.ImageField(upload_to='about_page')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Страницы О нас'


class AboutAdvantages(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    image = models.ImageField(upload_to='advantages')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Наши Примущество"