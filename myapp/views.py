from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  #save the student data to database
            return redirect('/list_student/')

    data = {
        'form': form
    }
    return render(request, "create_list.html", data)

def update_student(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/list_student')
              
    data = {
        'form': form
    }
    return render(request, "update.html", data)


def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/list_student")