import json
import sqlite3
import cgi

form = cgi.FieldStorage()
xml_string = form.getfirst("xml")

con = sqlite3.connect('software.db')
cur = con.cursor()

root = json.loads(xml_string)
table = root['name']
columns = root['structure']
table_body = ""
fkeys = ""
for column in columns:
    table_body += column['name']
    column_info = column['info'].split()
    table_body += " " + column_info[0]
    if column_info[1] == "1":
        table_body += " PRIMARY KEY"
    if column['name'] == "id":
        table_body += " AUTOINCREMENT"
    table_body += ', '
    if len(column_info) == 4:
        fkeys += f"FOREIGN KEY ({column['name']}) REFERENCES {column_info[-2]} ({column_info[-1]}), "
table_body += fkeys
table_body = table_body[:-2]

cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ( {table_body} );")
con.commit()

items = root['items']

print('Content-type: text/html\n')
for item in items:
    item_columns = item
    column_names = ", ".join([key for key in item.keys()])
    column_values = list(map(lambda value: f'"{value.strip()}"', [item_columns[key] for key in item_columns.keys()]))
    column_values = ", ".join(column_values)
    print(f"INSERT INTO {table} ({column_names}) VALUES ({column_values});")
    cur.execute(f"INSERT INTO {table} ({column_names}) VALUES ({column_values});")
con.commit()

con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')
