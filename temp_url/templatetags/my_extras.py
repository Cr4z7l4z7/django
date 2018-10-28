from django import template

register = template.Library()

@register.filter(name='cut')
def  cut(value, arg):
    """
    This cuts all vakues of "arg" from ther string!
    """
    return value.replace(arg,"")

# register.filter('cut',cut)
