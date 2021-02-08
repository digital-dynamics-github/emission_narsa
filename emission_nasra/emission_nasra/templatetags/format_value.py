from django import template
import types

register = template.Library()

@register.filter(name='format_value')
def formatValue(value):

    if isinstance(value, bytes) == True or isinstance(value, str) == True:
        return value
    else:
        value = str(value)
        if value.find(",") > -1:
            value = value.replace(",", ".")
        value = float(value)
        new_value = value
        new_value = round(new_value, 3)
        str_value = str(new_value)
        int_value = False
        if str_value.find(".") > -1:
            split_value = str_value.split(".")
            if int(split_value[1]) == 0 or split_value[1] == "0" :
                int_value = True
                value = int(new_value)
                new_value = int(new_value)


        if value > 1000:
            new_value = value/1000
            if int_value == False:
                new_value = round(new_value, 3)
            new_value = str(new_value)+" K"

        if value > 1000000:
            new_value = value/1000000
            if int_value == False:
                new_value = round(new_value, 3)
            new_value = str(new_value)+" M"

        if value > 1000000000:
            new_value = value/1000000000
            if int_value == False:
                new_value = round(new_value, 3)
            new_value = str(new_value)+" B"

        return new_value



#register.filter('format_value', formatValue)