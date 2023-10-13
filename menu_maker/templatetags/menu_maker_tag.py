from django import template

from menu_maker.models import Menu

register = template.Library()


@register.inclusion_tag('menu_maker/menu_sample.html', takes_context=True)
def draw_menu(context, slug):

    menu = Menu.objects.get(slug=slug)
    items = menu.menu_items.filter(parent_item=None)
    path = context['request'].resolver_match.view_name
    upper_levels, upper_active_items = [], []

    if menu.menu_items.filter(path=path).exists():
        current_item = menu.menu_items.get(path=path)
        current_item_children_items = current_item.children_items.all()

        temp_item = current_item
        while temp_item.parent_item:
            upper_active_items.append(temp_item.parent_item)
            upper_levels.append(temp_item.parent_item.children_items.all())
            temp_item = temp_item.parent_item

    else:
        current_item, current_item_children_items = None, None

    menu_dict = {
        'menu_title': menu.title,
        'items': items,
        'current_item': current_item,
        'upper_levels': upper_levels,
        'upper_active_items': upper_active_items,
        'current_item_children_items': current_item_children_items,
    }
    return menu_dict


@register.filter
def pop(value):
    value.pop()
    return value
