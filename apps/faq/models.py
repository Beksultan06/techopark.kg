from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class FAQCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы FAQ'



class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name='faqs')
    answer = RichTextField()
    question = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Часто задаваемые вопросы'