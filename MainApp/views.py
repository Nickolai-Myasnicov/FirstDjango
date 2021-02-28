from django.shortcuts import render, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item

user = {
    "name": "Николай",
    "middle": "Александрович",
    "surname": "Мясников",
}

'''
items = [
    {"id": 1, "name": "Кросовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 1},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 2},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 5},
]
'''

'''
def main(request):
    text = '<h1>"Изучаем django"</h1><br /> \
           <strong>Автор</strong>: <i>'{user["surname"]}{user["name"][0] .user["middle"]}'</i>'
    return HttpResponse(text)
'''

def main(request):
    return render(request, 'index.html')

def about(request):
    text = f"""
    Имя: {user['name']}<br>
    Отчество: {user['middle']}<br>
    Фамилия: {user['surname']}<br>
    """
    return HttpResponse(text)

'''
def show_item(request, id):
    current_item = None
    for item in items:
        if item['id'] == id:
            current_item = item

    if current_item is None:
        return HttpResponse(f"Товар с if {id} не найден")
    context = {
        "item": current_item
    }
    return render(request, "item.html", context)
'''

def show_item(request, id):
    try:
        current_item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": current_item
    }
    return render(request, "item.html", context)

'''def items_list(request):
    text = ""
    num = 1
    for item in items:
        text += f"{num}. {item['name']} <br>"
        num += 1
    return HttpResponse(text)
'''

'''def items_list(request):
    context = {
        "items": items
    }
    return render(request, "items.html", context)
'''

def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)