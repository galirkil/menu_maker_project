from typing import Any, Dict

from django import template
from django.template import Context

from menu_maker.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_maker/menu_sample.html', takes_context=True)
def draw_menu(context: Context, slug: str) -> Dict[str, Any]:
    all_items = MenuItem.objects.filter(menu__slug=slug).select_related(
        'parent_item')
    path = context['request'].resolver_match.view_name
    current_item, current_item_children_items = None, None
    menu_list, upper_levels, upper_active_items = [], [], []

    for i in all_items:
        menu_list.append(
            {
                'id': i.id,
                'title': i.title,
                'path': i.path,
                'parent_item': i.parent_item.id if i.parent_item else None,
                'children': [],
            }
        )

    for i in menu_list:
        for j in menu_list:
            if j['parent_item'] == i['id']:
                i['children'].append(j)

    items = [i for i in menu_list if i['parent_item'] is None]

    for i in menu_list:
        if i['path'] == path:
            current_item = i

    for i in menu_list:
        if i['id'] == current_item['id']:
            current_item_children_items = i['children']

    temp_item = current_item
    while temp_item and temp_item['parent_item']:
        upper_active_items.append(temp_item['parent_item'])
        for i in menu_list:
            if i['id'] == temp_item['parent_item']:
                upper_levels.append(i['children'])
        for i in menu_list:
            if i['id'] == temp_item['parent_item']:
                temp_item = i

    menu_dict = {
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
