from django import template
register = template.Library()


def modify_name(value, args):
    if args == 'first_name':
        return value.split(" ")[0]
    if args == 'last_name':
        return value.split(" ")[-1]
    if args == 'title_case':
        return value.title()

def define_number(value, args):
    if args == 'double':
        return value*2
    if args == 'triple':
        return value*3
    return value


register.filter('modify_name', modify_name)
register.filter('define_number', define_number)