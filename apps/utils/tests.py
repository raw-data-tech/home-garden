from django.test import TestCase


def console_log(param1, param2):
    color1 = '\033[94m'
    color2 = '\033[92m'
    end = '\033[0m'
    print color1 + param1 + end + '  ' + color2 + param2 + end 