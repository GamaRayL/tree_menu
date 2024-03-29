from django import template
from django.utils.safestring import mark_safe

from tree_menu.models import Menu

register = template.Library()


def draw_menu_recursive(items, current_path):
    """
        Функция рекурсивно строит дерево меню из ul и li тега,
            и возвращает результат в HTML формате.

        Параметры:
            items = список объектов из базы данных.
            current_path = текущий url путь.
    """
    result = []
    for item in items:
        url = item.get_absolute_url()
        is_active = current_path.startswith(url)

        result.append(f'<li>')
        result.append(f'<a style="color: black" href="{url}">{item.title}</a>')

        children = item.items.all()
        if children and is_active:
            result.append(f'<ul>')
            result.append(draw_menu_recursive(children, current_path))
            result.append('</ul>')
        result.append('</li>')
    return mark_safe(''.join(result))


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
        Функция принимает из шаблона контекст и заголовок меню, которого нужно отобразить.

        Параметры:
            context = контекст текущей страницы.
            menu_name = заголовок меню из базы данных (если не совпадает, то выведет все меню).
    """
    request = context.get('request')
    current_path = request.path
    menu_items = list(Menu.objects.prefetch_related('items').filter(title=menu_name)
                      or Menu.objects.prefetch_related('items').all())
    menu_html = draw_menu_recursive(menu_items, current_path)

    return menu_html
