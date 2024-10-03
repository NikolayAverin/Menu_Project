from django import template
from menu.models import Menu


register = template.Library()

def get_active_menus(menu_title, current_path):
    """Получаем активные меню."""
    active_menus = set()
    menus = Menu.objects.filter(title=menu_title)

    for menu in menus:
        if menu.url == current_path:
            active_menus.add(menu)
            while menu.parent:
                menu = menu.parent
                active_menus.add(menu)

    return active_menus

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_title):
    """Тэг для вставки меню."""
    current_path = context["request"].path
    active_menus = get_active_menus(menu_title, current_path)
    menus = Menu.objects.filter(title=menu_title)
    return {
        "menus": menus,
        "active_menus": active_menus
    }
