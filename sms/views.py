from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .form import StudentRegistrationForm
from .models import Student

# Create your views here.


class StudentCreate(CreateView):
    model = Student
    form_class = StudentRegistrationForm
    success_url = '/view'
    template_name = "StudentCourseRegistration/create.html"


class StudentDelete(DeleteView):
    model = Student
    fields = "__all__"
    success_url = "/view"


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentRegistrationForm
    success_url = "/view"
    template_name = "StudentCourseRegistration/create.html"

def viewStudent(request):
    objectList = Student.objects.all
    print(objectList)
    context = {"objectList":objectList}
    print(context)
    return render(request, "StudentCourseRegistration/view.html", context)