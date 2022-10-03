from django.shortcuts import render
from django.http import HttpResponse
from vininfo import Vin

"""
    def index(request):
        host = request.META["HTTP_HOST"]
        user_agent = request.META["HTTP_USER_AGENT"]
        path = request.path

        return HttpResponse(
            f""!
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User-agent: {user_agent}</p>""!
        )

    def index1(request, a, b, c):
        return HttpResponse(
            f""!<h1>Hi {a}, please wait</h1>
                <h1>Hi {b}, please wait</h1>
                <h1>Hi {c}, please wait</h1>""!)

    def contacts(request):
        return HttpResponse("<h1>+3752900000, +3754400000</h1>")
        
"""
def index(request):
    a = request.GET.get("name", "Who")
    b = request.GET.get("age", 40)

    return HttpResponse(
        f"""
            <h2><p>name: {a}</p></h2>
            <h2><p>age: {b}</p></h2>
            
            """
    
        )
        
def user(request, name, age):
    return HttpResponse(
        f"""<h2>Hi, {name} </h2> 
            <h2>You Age: {age} </h2>"""
    )

def products(request):
    return HttpResponse(
        f"""<h1>MASTER LIST</h1>"""

    )

def new(request):
    return HttpResponse(
        f"""<h1>NEW LIST</h1>"""

    )

def top(request):
    return HttpResponse(
        f"""<h1>TOP LIST</h1>"""

    )

def vininfo(request, Vin):
    vin = {Vin}
    return HttpResponse(
        f"""vin.annotate()
        code = vin.country_code
        valid = vin.verify_checksum()"""
    )


# Create your views here.
