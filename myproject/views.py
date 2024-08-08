from django.shortcuts import HttpResponse, render 
from random import randint

def index_view(request):
    # return HttpResponse("This is Home Page")
    random_data = randint(1,100)

    data = {
        "name": "Prakash Rajbanshi",
        "address": "Kachankawal",
        "age": 20 ,
        "gender": "Male",
        "description": "Hello everyone my name is prakash rajbanshi i m from kachnakawal",
        "random_no":random_data,
        "hobbies": ["Dancing", "Singing", "Codding", "football", "Swimming"]
    }
    return render(request, "index.html" , data)

def login_view(request):
    # return HttpResponse("This is login Page!")
    return render(request, "login.html")


def register_view(request):
    return HttpResponse("This is register Page! You can register here!")