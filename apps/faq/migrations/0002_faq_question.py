# Generated by Django 4.2 on 2025-05-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='question',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
