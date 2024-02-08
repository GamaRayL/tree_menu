from django.views.generic import ListView

from tree_menu.models import Menu


class MenuListView(ListView):
    model = Menu
    extra_context = {
        'title': 'Список древовидных меню'
    }
