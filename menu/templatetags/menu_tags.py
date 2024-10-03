from django import template
from django.template.context_processors import request
from django.urls import resolve
from menu.models import Menu


register = template.Library()

def get_current_menu(request):
    """Получение текущего меню."""
    current_url = request.path
    return Menu.objects.filter(url=current_url).first()

def generate_menu(menu_title, active_menu):
    """Генерирование меню."""
    menu_items = Menu.objects.filter(parent__isnull=True)

    active_menus = []
    if active_menu:
        active_menus.append(active_menu)
        while active_menu.parent:
            active_menu = active_menu.parent
            active_menus.append(active_menu)

    return {
        "menu_items": menu_items,
        "active_menus": active_menus,
        "menu_title": menu_title,
    }

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_title):
    """Вызов сгенерированного меню."""
    request = context["request"]
    current_menu = get_current_menu(request)
    return generate_menu(menu_title, current_menu)
