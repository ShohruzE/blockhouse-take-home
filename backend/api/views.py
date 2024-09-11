from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Test view 
@api_view(['GET'])
def home(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def candlestick_data(request):
    data = [
        {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
        {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
    ]
    return Response(data)

@api_view(['GET'])
def line_chart_data(request):
    data = [
        {"name": "Jan", "value": 10},
        {"name": "Feb", "value": 20},
        {"name": "Mar", "value": 30},
        {"name": "Apr", "value": 40},
    ]
    return Response(data)

@api_view(['GET'])
def bar_chart_data(request):
    data = [
        {"name": "Product A", "value": 100},
        {"name": "Product B", "value": 150},
        {"name": "Product C", "value": 200},
    ]
    return Response(data)

@api_view(['GET'])
def pie_chart_data(request):
    data =  [
        {"name": "Red", "value": 300},
        {"name": "Blue", "value": 50},
        {"name": "Yellow", "value": 100},
    ]
    return Response(data)
