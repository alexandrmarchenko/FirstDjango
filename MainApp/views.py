from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
name = "Александр"
middlename = "Васильевич"
lastname = "Марченко"
tel = "8-923-600-01-02"
email = "django@mail.ru"

items_list = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = f"""<h1>"Изучаем django день первый"</h1>
            <strong>Автор</strong>: <i>{lastname} {name[:1]}.{middlename[:1]}.</i>"""
    return HttpResponse(text)

def about(request):
    text = f"""Имя: <b>{name}</b><br>
            Отчество: <b>{middlename}</b><br>
            Фамилия: <b>{lastname}</b><br>
            телефон: <b>{tel}</b><br>
            email: <b>{email}</b>"""
    return HttpResponse(text)

def items(request):
    text = ""
    for idx, item in enumerate(items_list):
        text += f"""<a href="/item/{item["id"]}"> {idx+1}. {item["name"]} </a><br>"""
    return HttpResponse(text)

def show_item(requets, item_id):
    text = "<a href='/items/'> <назад к списку товаров </a> <br><br>"
    item = next((x for x in items_list if x["id"] == item_id), None)
    if item is None:
        text += f"Товар с id={item_id} не найден"
    else:
        text += f"""<b>Товар</b>: {item["name"]} <br>
                <b>Количество</b>: {item["quantity"]}"""
    return HttpResponse(text)
