from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1><b>FTW! ACAB!</b></h1>")

def index1(request, a, b, c):
    return HttpResponse(
        f"""<h1>Hi {a}, please wait</h1>
            <h1>Hi {b}, please wait</h1>
            <h1>Hi {c}, please wait</h1>""")

def contacts(request):
    return HttpResponse("<h1>+3752900000, +3754400000</h1>")

# Create your views here.
