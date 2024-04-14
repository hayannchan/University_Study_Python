import sqlite3

connection = sqlite3.connect('software.db')
cursor = connection.cursor()
cursor.executescript(open('db_creation.sql').read())
cursor.executescript(open('db_insertion.sql').read())
# Every version of Windows released
res = cursor.execute('''
SELECT 
    ver.version
FROM 
    Versions ver
JOIN 
    Software soft ON soft_name = soft.id_s
WHERE 
    soft.name = "Windows";
''')
print(res.fetchall())
# Amount of Versions on each Microsoft product
res = cursor.execute('''
SELECT 
    soft.name, COUNT(*)
FROM 
    Versions ver
JOIN 
    Software soft ON soft_name = soft.id_s
JOIN 
    Corporation co ON developer = co.id_c
WHERE 
    co.name = "Microsoft"
GROUP BY soft.name;
''')
print(res.fetchall())
# The biggest amount of released versions
res = cursor.execute('''
SELECT MAX(c)
FROM (SELECT 
    co.name, COUNT(*) c
FROM 
    Versions ver
JOIN 
    Software soft ON soft_name = soft.id_s
JOIN 
    Corporation co ON developer = co.id_c
GROUP BY co.name)
''')
print(res.fetchall())