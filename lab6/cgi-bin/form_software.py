import cgi
import sqlite3

form = cgi.FieldStorage()
name = form.getfirst("soft_name")
developer = form.getfirst("soft_developer")
if developer:
    developer = int(developer)
con = sqlite3.connect("software.db")
cur = con.cursor()

if all((name, developer)):
    query = f"INSERT INTO Software (name, developer) VALUES ('{name}', {developer})"
    cur.execute(query)
    con.commit()
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')