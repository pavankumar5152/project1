from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse("""<html><body bgcolor=cyan><center><h1>welcome to pavan</h1></center></body><html>""")

