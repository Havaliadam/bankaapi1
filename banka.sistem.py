import sqlite3
import random as r 
class Bank:
    print("sayın müşteri hosgeldiniz")
    def __init__(self):
        self.con=sqlite3.connect("admin.db")
        self.c=self.con.cursor()
    def kayıtolustur(self):

        self.c.execute("""CREATE TABLE IF NOT EXISTS müsteri(numara numerıc,sifre numeric,id integer,müsisim,"email"TEXT,
	    "dogumta"	NUMERIC,
	    "cinsiyet"	BLOB)

        """)
       
        n1=input("numara giriniz:-")
        n2=input("sifre olusturun:-")
        n3=input("isim giriniz : -").upper()
        n4=input("id giriniz:")
        n5=input("email giriniz:")
        n6=input("dogum tarihi giriniz:")
        n7=input("cinsiyeti giriniz:").upper()
        if n1.isdigit() and not n1.isdigit() and n2.isdigit() and not n2.isdigit() and n3.isalpha() and not n3.isspace() and n4.isdecimal() and not n4.isdecimal() and  n5.isalpha() and not n5.isspace()  and   n6.isalpha() and not n6.isspace() and n7.isalpha() and not n7.isspace():
            bil=n3+''+n5+''+n6+''+n7
            num=r.randint(100000,9999999) 
            self.c.cursor("INSERT INTO müsteri VALUES (?,?,?,?,?,?,?)",(bil,num))
            print(" sayın {} müşteri eklendi".format(bil))
            print("lütfen  numara yı girin{}".format(num))
            
            
            self.con.commit()
            self.con.close()
            "self.c.execute(""select * from müsteri"")"
         
        else:
            print("bilgileri girin")
                    
    def bankagiris(self):
        a_numara=int(input("numarayı girin"))
        check=True
        for a,b,c in self.c.execute("select  * from müsteri"):
            if b== a_numara:
              check=False
            if check:
                print("hatalı numara")
                




bk=Bank()
#bk.kayıtolustur()        
bk.bankagiris()
