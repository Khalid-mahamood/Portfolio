# Generated by Django 3.2.16 on 2022-12-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='Projects')),
            ],
        ),
    ]
