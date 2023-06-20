from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def debugger(request):
    return render(request, 'debugger.html')
