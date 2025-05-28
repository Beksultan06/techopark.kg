from django.db import models
from apps.settings.icon import ICON

# Create your models here.
class BaseBanner(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Баннера'
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    button_text = models.CharField(max_length=100, default="Contact Us")
    button_link = models.URLField(default='/contact.html')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Баннер в главной страницы'

class Settings(models.Model):
    title_about = models.CharField(
        max_length=155
    )
    description = models.TextField()
    image_author = models.ImageField(upload_to='settings')
    title_athor = models.CharField(
        max_length=155
    )
    title_manager = models.CharField(
        max_length=155
    )
    manager = models.CharField(
        max_length=155
    )
    description_about = models.TextField()
    title_services = models.CharField(
        max_length=155
    )
    description_service = models.TextField()
    title_cases = models.CharField(
        max_length=155
    )
    description_cases = models.TextField()
    title_static = models.CharField(
        max_length=155
    )
    description_static = models.TextField()
    image_static1 = models.ImageField(
        upload_to="settings"
    )
    image_static2 = models.ImageField(
        upload_to="settings"
    )
    title_news = models.CharField(
        max_length=155
    )
    description_news = models.TextField()
    title_contact = models.CharField(
        max_length=155
    )
    description_contact = models.TextField() 

    def __str__(self):
        return self.title_about

    class Meta:
        verbose_name_plural = 'Главная Настройки'

class Services(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField()
    icon = models.CharField(
        max_length=155,
        choices=ICON
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши услуги'

class Cases(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField()
    image = models.ImageField(upload_to='cases')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Случай'

class Statistic(models.Model):
    title = models.CharField(
        max_length=155
    )
    percent = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Наши статистики"

class News(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField()
    image = models.ImageField(upload_to='news')
    data = models.CharField(
        max_length=155
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши новости'

class Contact(models.Model):
    full_name = models.CharField(
        max_length=155
    )
    email = models.EmailField()
    type_info = models.CharField(
        max_length=155
    )
    message = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Форма Обратной связи'