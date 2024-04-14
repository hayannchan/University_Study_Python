from csv import DictReader

convertation = {"дн.": 86400, "час.": 3600, "мин.": 60, "сек.": 1}
def to_seconds(string = ""):
    l = string.split(" ")
    s = 0
    for i in range(int(len(l)/2)):
        s += int(l[2*i])*convertation[l[2*i+1]]
    return s
f = open("15 - 1.csv", encoding="utf8")
completed = set()
reader = DictReader(f)
limit_time = to_seconds(input())
for row in reader:
    if row["Фамилия"] == "Среднее по группе":
        break
    converted = to_seconds(row["Затраченное время"])
    undone = set()
    for i in range(1,11):
        if row[f"В. {i} /1,00"] == "0,00":
            undone.add(i)
    undone_check = False
    task_categories = [(1,2), (3,), (4,5), (6,7), (8,9,10)]
    for categ in task_categories:
        if set(categ).issubset(undone):
            undone_check = True
    if converted < limit_time and undone_check:
        completed.add(row["Фамилия"]+" "+row["Имя"])
print(len(completed))