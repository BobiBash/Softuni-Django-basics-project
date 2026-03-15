from django import template

register = template.Library()

@register.filter(name='format_date')
def format_date(value):
    return value.strftime('%d/%m/%Y')

@register.filter(name='lat_lon_format')
def lat_lon_format(value):
    return f"{value:.2f}°"