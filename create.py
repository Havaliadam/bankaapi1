import sqlite3

connection=sqlite3.connect("admin.db")
cursor=connection.cursor()

command="""CREATE TABLE IF NOT EXISTS müsteri(numara numerıc,sifre numeric,id  integer ,müsisim,"email"TEXT,
	"dogumta"	NUMERIC,
	"cinsiyet"	BLOB)

"""




cursor.execute("INSERT INTO müsteri VALUES(5,'ali','ali@gmail.com','18-03-1985','e','5344558796','5236850')")

connection.commit()



#'5368746523','12345678',2,'hakkı','e','28-09-1975','hakkı@gmail.com'