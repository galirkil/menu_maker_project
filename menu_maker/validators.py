from django.core.exceptions import ValidationError
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


def validate_path(instance):
    try:
        reverse(instance.path)
    except NoReverseMatch:
        raise ValidationError(
            {'path': 'Указанный адрес не зарегистрирован', }
        )


def validate_menu(instance):
    if (instance.parent_item
            and instance.parent_item not in instance.menu.menu_items.all()):
        raise ValidationError(
            {
                'parent_item':
                    'Родительский пункт должен быть '
                    'из того же меню что и дочерний',
            }
        )


def validate_parent(instance):
    if instance.parent_item == instance:
        raise ValidationError(
            {
                'parent_item':
                    'Пункт меню не может быть родителем для самого себя',
            }
        )
