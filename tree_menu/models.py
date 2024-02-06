from django.db import models

from constants import NULLABLE


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='меню')
    branch = models.ForeignKey('self', **NULLABLE, verbose_name='ветка')

    def __str__(self):
        return self.name
