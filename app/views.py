from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def misba(request):
    return HttpResponse('misba is my elder sister')
def amrin(request):
    return HttpResponse('<h1> iam doing django project </h1>')
def arhaan(request):
    return HttpResponse('<h1><marquee> king of the family <h1><marquee>')
def samantha(request):
    return HttpResponse('''<h1>samantha<h1><i>age is 32</i> <b>she is Good actor</b> <img src='https://cf-img-a-in.tosshub.com//sites//visualstory//wp//2024/08/iPhone-16-Pro.jpeg?size=*:900" alt="">''')