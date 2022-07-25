import sqlite3

con = sqlite3.connect("database.db")
print("The database is opened!")
cur = con.cursor()
sql='''CREATE TABLE "students" (
"SID" INTERGER,
"name" TEXT,
"grade" INTERGER
)'''

cur.execute(sql)
con.commit()

con.close()
