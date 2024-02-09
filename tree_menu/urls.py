from django.urls import path
from django.views.decorators.cache import cache_page

from tree_menu.apps import TreeMenuConfig
from tree_menu.views import MenuListView

app_name = TreeMenuConfig.name

urlpatterns = [
    path('', cache_page(60 * 15)(MenuListView.as_view()), name='menu_list'),
    path('<path:slug>/', cache_page(60 * 15)(MenuListView.as_view()), name='draw_menu'),
]
