import re

def func(str):
    dct = {}
    a = str.split("</section>")[:-1]
    print(a)
    for text in a:
        temp_key = ""
        start_key = text.find("'") + 1
        while (text[start_key] != "'"):
            temp_key += text[start_key]
            start_key += 1
        dct[temp_key] = []
        start_val = text.find('{') + 1
        end_val = text.find('}')
        values = text[start_val:end_val].split(';')
        print(values)
        for value in values:
            dct[temp_key].append(int(value.strip()[1:]))

    return dct


str = "<section> {#-5126 ; #9937 ; #-8638 } to'isge_751'.</section><section> { #9929 ; #6707 ; #-4475 } to'edenus_286'.</section> <section> { #6198 ;#96 } to 'soenis'.</section> "

print(func(str))
