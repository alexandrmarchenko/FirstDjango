from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    text = """<h1>"Изучаем django день первый"</h1>
            <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)
