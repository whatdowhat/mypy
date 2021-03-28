from django.shortcuts import render
from django.http import HttpResponse
from .models import StockComeR

# Create your views here.
def index(request):

    stockComeR = StockComeR.objects.all()
    print(stockComeR)
    return HttpResponse("Hello, world. You're at the polls index.")


