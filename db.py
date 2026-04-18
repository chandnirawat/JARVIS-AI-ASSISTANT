import sqlite3
con = sqlite3.connect("jarvis.db")
import os
print("DB FILE:", os.path.abspath("jarvis.db"))
cursor = con.cursor()


# Table create
query = "CREATE TABLE IF NOT EXISTS SYS_COMMAND(ID INTEGER PRIMARY KEY, NAME VARCHAR(100), PATH VARCHAR(1000))"
cursor.execute(query)

# Insert data (fixed)
#query = "INSERT INTO SYS_COMMAND VALUES (null, 'ONENOTE', 'C:\\program files\\microsoft office\\root\\office16\\ONENOTE.exe')"
#cursor.execute(query)

#con.commit()

query = "CREATE TABLE IF NOT EXISTS WEB_COMMAND(ID INTEGER PRIMARY KEY, NAME VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO WEB_COMMAND VALUES (null, 'canva', 'https://www.bing.com/search?q=canva.com&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=canva.com&sc=12-9&sk=&cvid=F1C2678CBF5D44DB962E605D6F0442AB')"
cursor.execute(query)

con.commit()






