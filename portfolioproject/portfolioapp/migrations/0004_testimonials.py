# Generated by Django 3.2.16 on 2022-12-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_rename_img_projects_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Des', models.TextField()),
                ('image', models.ImageField(upload_to='Testimonial')),
            ],
        ),
    ]