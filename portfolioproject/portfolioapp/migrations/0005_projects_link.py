# Generated by Django 3.2.16 on 2022-12-03 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Link',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
