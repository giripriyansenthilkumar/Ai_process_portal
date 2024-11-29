import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from pymongo import MongoClient
from pdf2image import convert_from_path
import easyocr
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'aippapp/home.html')

def app1(request):
    return render(request, 'aippapp/app1.html')

def app2(request):
    return render(request, 'aippapp/app2.html')

def app3(request):
    return render(request, 'aippapp/app3.html')

def app4(request):
    return render(request, 'aippapp/app4.html')
 
def reg(request):
    return render(request,'aippapp/reg.html')

def login(request):
    return render(request, 'aippapp/login.html')

