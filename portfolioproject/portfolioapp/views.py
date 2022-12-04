from django.shortcuts import render,redirect
from .models import service, Projects,Testimonials

# Create your views here.


def index(request):
    Service = service.objects.all()
    Project = Projects.objects.all()
    Testimonial=Testimonials.objects.all()
    return render(request, 'index.html',{'Service':Service,'Project':Project,'Testimonial':Testimonial})
def reg(request):
    return render(request,'Feedback.html')

def add(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Des = request.POST.get("Des")
        image = request.FILES["image"]
        Testimonial= Testimonials(Name=Name, Des=Des,  image=image,)
        Testimonial.save()
        return redirect('/')
    return render(request, "Feedback.html")