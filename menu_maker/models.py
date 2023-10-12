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
            'Укажите уникальный идентификатор для меню. '
            'Значение этого поля используется для загрузки меню в шаблон. '
            'Допустимы латинские буквы, цифры и нижнее подчеркивание'

        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Введите название для пункта меню',
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name='Меню',
        help_text='Выберите меню в которое будет добавлен данный пункт'
    )
    path = models.CharField(
        'Адрес пункта меню',
        max_length=256,
        help_text=(
            'Введите адрес пункта меню. '
            'Формат: namespace:name'
        )
    )
    parent_item = models.ForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children_items',
        verbose_name='Родительский пункт меню',
        help_text=(
            'Выберите родительский пункт меню. '
            'Родительский пункт должен относиться к выбранному меню. '
            'Значение по умолчанию создаст '
            'корневой пункт меню.'
        )
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
