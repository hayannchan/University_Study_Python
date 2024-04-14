import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("co_name")
year = form.getfirst("co_year")
if year:
    year = int(year)
con = sqlite3.connect("software.db")
cur = con.cursor()

if all((name, year)):
    query = f"INSERT INTO Corporation (name, year) VALUES ('{name}', '{year}')"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')