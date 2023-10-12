from django.db import models


class Menu(models.Model):

    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Введите название для меню',
    )

    slug = models.SlugField(
        'Человекопонятный идентификатор',
        max_length=256,
        unique=True,
        help_text=(
            "Укажите уникальный идентификатор для меню. "
            "Значение этого поля используется для загрузки меню в шаблон. "
            "Допустимы латинские буквы, цифры и нижнее подчеркивание"

        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


