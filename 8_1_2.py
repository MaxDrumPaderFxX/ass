import re


def func(str):
    dick = {}
    a = str.split("end, ")[:-1]
    # print(a)
    for key in a:
        temp_key = re.search(r"var\s*([a-zA-z0-9_])+\s*", key).group(0)[4:].strip()
        # print(temp_key)
        temp_val = re.search(r"[#]([+-])*([0-9])+", key).group(0)[1:].strip()
        # print(temp_val)
        dick[temp_key] = int(temp_val)

    return dick


str = "<data> begin var ceceti_326 <= #-4238. end, begin var vein<= #8127.end, </data>"
print(func(str))
