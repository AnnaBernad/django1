from django.shortcuts import render

# Create your views here.

def calc(request, x, act, y):
    wrong = None
    res = None
    if act == "*":
        res = x * y
    elif act == "div":
        res = x / y 
    elif act == "+":
        res = x +y
    elif act =="-":
        res = x - y
    else:
        wrong = "wrong"
    return render(request, 'calculator/calc.html', {"x": x, "act": act, "y": y, "res": res, "wrong": wrong})
        


