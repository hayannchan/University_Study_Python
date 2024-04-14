import re

def is_zip(string):
    reg_exp_zip = re.compile('[0-9]{5}(?:-[0-9]{4})')
    result = reg_exp_zip.match(string)
    return result != None and result.group() == string

def zip_with_exception(string):
    if not is_zip(string): 
        raise AttributeError("String is not ZIP Code")
    return string

print(is_zip("12345-6789"))
try:
    print(zip_with_exception("54321--1453"))
except (AttributeError) as e:
    print(e)