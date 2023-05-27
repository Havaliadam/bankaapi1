import sqlite3

with sqlite3.connect("admin.db")as com:
    
    com.row_factory=sqlite3.Row
    cur=com.cursor()
    cur.execute("SELECT numara,sifre from müsteri")
    rows=cur.fetchall() 
    
    
    


