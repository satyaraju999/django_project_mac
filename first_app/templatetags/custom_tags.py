from django import template
from django.contrib.auth import get_user_model
from django.template.loader import get_template
register = template.Library()
from datetime import datetime
from first_app.models import Department

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

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

# Depart = get_user_model()



@register.inclusion_tag('first_app/latest.html')
def show_depart_table():
    departs = Department.objects.all()
    return {'departments': departs}



register.filter('modify_name', modify_name)
register.filter('define_number', define_number)