from django.db import models

# Create your models here.
class service(models.Model):
    Name = models.CharField(max_length=250)
    Des = models.TextField()
    img = models.ImageField(upload_to='Service')

    def __str__(self):
        return self.Name

class Projects(models.Model):
    Name=models.CharField(max_length=50)
    image= models.ImageField(upload_to='Projects')
    Link = models.TextField()


    def __str__(self):
        return self.Name
class Testimonials(models.Model):
    Name=models.CharField(max_length=30)
    Des=models.TextField()
    image=models.ImageField(upload_to='Testimonial')

    def __str__(self):
        return self.Name