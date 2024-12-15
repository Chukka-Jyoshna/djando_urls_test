from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Adding(request,n1,n2):
    n3=int(n1)+int(n2)
    mes=f'<h2>adding of {n1} and {n2} is {n3} </h2>'
    response=HttpResponse(mes)
    return response 
def subtraction(request,n1,n2):
    n3=int(n1)-int(n2)
    mes=f'<h2> subtraction of {n1} and {n2} is {n3}</h2> '
    response=HttpResponse(mes)
    return response
