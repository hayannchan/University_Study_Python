def check(string):
    s = string.split()
    if len(s) != 3: return False
    if s[1] not in ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]: return False 
    if not s[0].isnumeric(): return False
    if not s[2].isnumeric(): return False
    if int(s[0]) < 1 or int(s[0]) > 31: return False
    return True

def findDates(string):
    l = string.split()
    r = []
    for i in range(len(l)-2):
        j = " ".join([l[i], l[i+1], l[i+2]])
        if check(j):
            r.append(j)
    return r
