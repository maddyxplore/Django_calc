from django.shortcuts import render,redirect
from .models import User,Login
from django.contrib.auth.models import auth
# Create your views here.

def index(request):
    if request.method == "POST":
        value1 = request.POST.get("value1")
        value2 = request.POST.get("value2")
        operation = request.POST.get("operation")
        res = ""
        if operation == "+":
            res = int(value1) + int(value2)
            res = "The Sum is: "+ str(res)
        elif operation == "-":
            res = abs(int(value1) - int(value2))
            res = "The Difference is: "+ str(res)
        elif operation == "*":
            res = int(value1) * int(value2)
            res = "The Product is: "+ str(res)
        return render(request, "index.html", {'res': res})
    return render(request, "index.html")

