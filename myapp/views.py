from django.shortcuts import render, redirect
from .models import Student , BloodRequest
from .forms import StudentForm, bloodRequestForm

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

def emergency_view(request):
    bloodrequests = BloodRequest.objects.filter(is_expired=False, is_verified=True)
    data ={
        'bloodrequests': bloodrequests
    }
    return render(request, "emergency.html", data)

def add_blood_request(request):
    form = bloodRequestForm()
    if request.method == 'POST':
        form = bloodRequestForm(request.POST)
        if form.is_valid():
            form.save()  #save the student data to database
            return redirect('/emergency/')

    data = {
        'form': form
    }
    return render(request, "addbloodrequest.html", data)