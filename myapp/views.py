from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    data ={
        'students': students
    }
    return render(request, "student_list.html", data)

def create_list(request):

    print(request.POST)
    form = StudentForm()
    data = {
        'form': form
    }
    return render(request, "create_list.html", data)