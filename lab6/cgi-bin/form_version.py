import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("ver_name")
soft_name = form.getfirst("ver_soft_name")
if soft_name:
    soft_name = int(soft_name)
con = sqlite3.connect("software.db")
cur = con.cursor()

if all((name, soft_name)):
    query = f"INSERT INTO Versions (version, soft_name) VALUES ('{name}', {soft_name})"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')