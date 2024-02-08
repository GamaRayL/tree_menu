from django.urls import path

from tree_menu.apps import TreeMenuConfig
from tree_menu.views import MenuListView

app_name = TreeMenuConfig.name

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('<path:slug>/', MenuListView.as_view(), name='draw_menu'),
]
