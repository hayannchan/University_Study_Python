import sqlite3
import cgi
import json

form = cgi.FieldStorage()
table = form.getfirst("table")

root = {"name": table, "structure": [], "items": []}
structure = root['structure']
items =root['items']

con = sqlite3.connect('software.db')
cur = con.cursor()

try:
    cur.execute(f'SELECT * FROM {table}')
except sqlite3.OperationalError as e:
    print('Content-type: text/html\n')
    print(e)
    exit(0)

for row in cur.fetchall():
    item = {}
    items.append(item)
    # cur.description - кортежи, где содержатся имена столбцов
    for i, column_name in enumerate(cur.description):
        column_value = row[i]
        item[column_name[0]] = str(column_value)

cur.execute(f"PRAGMA foreign_key_list({table})")
fkeys = cur.fetchall()
cur.execute(f"PRAGMA table_info({table})")
for row in cur.fetchall():
    column = {"name": row[1]}
    structure.append(column)
    column_info = row[2] + " " + str(row[-1])
    for fk in fkeys:
        if fk[3] == row[1]:
            column_info += " " + fk[2] + " " + fk[4]
            break
    column['info'] = column_info

#xml_str = ET.dump(root)
# print(xml_str)
print("Content-type: text/html\n")

print(f"""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Exported address table</title>
        </head>
        <body>
            <textarea rows=50 cols=60>
{json.dumps(root, indent=2)}
      </textarea>
    """)

print("""</body>
        </html>""")

con.close()