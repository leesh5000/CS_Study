def pal(_str: string)->bool:
    if len(_str)<=1:
        return True
    if _str[0]==_str[-1]:
        return pal(_str[1:-1])
    else:
        return False

print(pal('level'))