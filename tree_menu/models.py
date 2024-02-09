from django.db import models
from django.urls import reverse

from constants import NULLABLE


class Menu(models.Model):
    """Модель меню"""
    title = models.CharField(max_length=150, verbose_name='Заголовок меню')
    slug = models.SlugField(max_length=255, unique=True, null=False, verbose_name='Слаг')

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tree_menu:draw_menu', kwargs={'slug': self.slug})


class MenuItem(models.Model):
    """
        Модель ветки меню.
        Поля:
            title (str): Заголовок ветки меню.
            menu (Menu): Внешний ключ для связи с родительским меню.
            parent (MenuItem): Внешний ключ для связи с родительским элементом меню.
            slug (str): Уникальный слаг для идентификации элемента меню.

        Методы:
            get_absolute_url():
                Возвращает абсолютный URL элемента меню, включая URL родительских элементов и базового меню.
    """
    title = models.CharField(max_length=100, verbose_name='Заголовок ветки')
    menu = models.ForeignKey(Menu, related_name='items',
                             **NULLABLE,
                             verbose_name='Меню',
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self',
                               **NULLABLE,
                               related_name='items',
                               verbose_name='Родитель ветки',
                               on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null=False, verbose_name='Слаг')

    class Meta:
        verbose_name = 'ветка меню'
        verbose_name_plural = 'ветки меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = [self.slug]
        current_item = self

        while current_item.parent:
            url.insert(0, current_item.parent.slug)
            current_item = current_item.parent

        if current_item.menu:
            base_menu_url = current_item.menu.get_absolute_url()
            return f"{base_menu_url}{('/'.join(url))}"
