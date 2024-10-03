from django.db import models


class Menu(models.Model):
    """Модель меню."""
    title = models.CharField(max_length=100, verbose_name="Название меню")
    url = models.URLField(null=True, blank=True, verbose_name="Ссылка")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children", verbose_name="Вышестоящий уровень меню")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
