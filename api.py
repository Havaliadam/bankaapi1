
from flask import g 
from flask import Flask,render_template,url_for,request,redirect,flash,session,g# kütüphaneler
import sqlite3# veri tabanını dahil ettik

app = Flask(__name__)
  
def giris_admin_db(numara,sifre,id): #burada  fonksiyon tanımlarım method atadık
       connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
       cursor=connection.cursor() #bağlatımızı ile imleç oluştuyoruz
       cursor.execute("insert into müsteri(id,numara,sifre) values(?,?,?)",(sifre,numara,id)) # sorgu işlemi
       connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
       connection.close()# sorgumuzu kapattık
def giris(numara,sifre,id):
        connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
        cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
        cursor.execute('SELECT numara sifre FROM müsteri WHERE numara=? and sifre=? and id=?',(numara,sifre,id))# sorgu işlemi    
        result=cursor.fetchone()# verileri tek tek okumayı sağlar
        if result:
         return True
        else:
            return False
def müsterifatura_db(id,müsterihesapno):#burada  fonksiyon tanımlarım method atadık
     connection=sqlite3.connect("admin.db")# burada veri tabanımıza bağlandık
     cursor=connection.cursor()#imleç işlemini yapıyoruz
     cursor.execute("insert into müsterifatura(id,müsterihesapno) values(?,?)",(id,müsterihesapno))# imleç yolu ile sorgu işlemi yapıyoruz
     connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
     connection.close()# sorgumuzu kapattık
def fatura (id,müsterihesapno):
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()#imleç oluştuyoruz
     cursor.execute('SELECT id müsterihesapno FROM müsterifatura where id=? and müsterihesapno=? ',(id,müsterihesapno))#müşterifatura datamızın sorgu işlemini yapılır    
     result=cursor.fetchone()#verileri birbir okumayı sağlar
     if result:
        return True
     else:
        return False 
def müsteriistanbulkart_db(id,kartno,müsterihesapno):#burada  fonksiyon tanımlarım method atadık
      connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
      cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
      cursor.execute("insert into müsteriistanbulkart(id,kartno,müsterihesapno) values(?,?,?)",(id,kartno,müsterihesapno)) # sorgu işlemi
      connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
      connection.close()# sorgumuzu kapattık
      
def istanbulkart(id,kartno,müsterihesapno): # yeni bir fonksiyon oluşturduk
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()#imleç oluştuyoruz
     cursor.execute("SELECT id  kartno müsterihesapno FROM müsteriistanbulkart where id=? and kartno=?  andmüsterihesapno=? ",(id,kartno,müsterihesapno))#müşteriistanbulkart datamızın sorgu işlemini yapılır 
    
     result=cursor.fetchone()#verileri birbir okumayı sağlar
     if result:
        return True
     else:
        return False 
def müsteriparacekme_db(id,kartid,tutar):#burada  fonksiyon tanımlarım method atadık
     connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
     cursor=connection.cursor() #bağlatımızı ile imleç oluştuyoruz
     cursor.execute("insert into müsteriparacekme(id,kartid,tutar) values(?,?,?) ",(id,kartid,tutar))#sorgu işlemi
     connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
     connection.close()# sorgumuzu kapattık
def cekme(id,kartid,tutar):# yeni bir fonksiyon oluşturduk
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()#imleç oluştuyoruz
     cursor.execute("SELECT müsid  kartid tutar FROM müsteriparacekme where müsid=? ,kartid=?  and tutar=? ",(id,kartid,tutar))#müsteriparaçekme datasının sorgu işlemi
     result=cursor.fetchone()#verileri tek tek okumasını sağlar
     if result:
        return True
     else:
        return False 
def müsteriparayatırma_db(id,hesapid,limit):#burada  fonksiyon tanımlarım method atadık
     connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
     cursor=connection.cursor() #bağlatımızı ile imleç oluştuyoruz
     cursor.execute("insert into müsteriparayatırma(id,hesapid,limit) values(?,?,?) ",(id,hesapid,limit))#sorgu işlemi yapılır
     connection.commit()#bağlatımızı ile imleç oluştuyoruz
     connection.close()#sorgumuzu kapaltık
def parayatırma(id,hesapid,limit):# yeni bir fonksiyon oluşturduk
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()#imleç oluştuyoruz
     cursor.execute("SELECT id  hesapid limit FROM müsteriparayatırma where id=? , hesapid=?  and limit=? ",(id,hesapid,limit))#müsteriparayatırma datasınada sorgulama işlemi yapılması
     result=cursor.fetchone()#verileri tek tek okuması sağlar
     if result:
        return True
     else:
        return False       
def müsterikredihesaplama_db(id,tutar,hesap):#burada  fonksiyon tanımlarım method atadık
     connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
     cursor=connection.cursor() #bağlatımızı ile imleç oluştuyoruz
     cursor.execute("insert into müsterikredibaşvuru(id,tutar,hesap) values(?,?,?)",(id,tutar,hesap))#sorgu işlemi yapılır
     connection.commit()#bağlatımızı ile imleç oluştuyoruz
     connection.close()#sorgumuzu kapaltık
def kredi(id,tutar,hesap):# yeni bir fonksiyon oluşturduk
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()# imleç oluşturması
     cursor.execute("SELECT id  tutar hesap FROM müsterikredibaşvuru where id=? and hesap=?  and tutar=? ",(id,hesap,tutar))#müsterikredibaşvuru datasında veri sorgulama işlemi yapılması
     result=cursor.fetchone()#verileri tek tek okuması
     if result:
        return True
     else:
        return False
def müsterihesapacma_db(id,hesapid,hesaptürü):#burada  fonksiyon tanımlarım method atadık
        connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
        cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
        cursor.execute("insert into müsterihesapacma(id,hesapid,hesaptürü) values(id,hesapid,hesaptürü)",(id,hesapid,hesaptürü))#sorgu işlemi yapılır    
        connection.commit()#bağlatımızı ile imleç oluştuyoruz
        connection.close()#sorgumuzu kapaltık    
        
def hesapacma(id,hesapid,hesaptürü):# yeni bir fonksiyon oluşturduk
        connection=sqlite3.connect("admin.db")#veri tabanımıza bağlandık
        cursor=connection.cursor() #imleç oluşturması
        cursor.execute("SELECT id  hesapid hesaptürü FROM müsterihesapacma where id=? and hesapid=?  and hesaptürü=? ",(id,hesapid,hesaptürü))#müsterihesapacma datasına veri sorgulama işlemi yapılması
        result=cursor.fetchone()#verileri tek tek okuması
        if result:
            return True
        else:
            return False   
def müsterihesapkapatma_db(id,hesapid,hesaptürü):#burada  fonksiyon tanımlarım method atadık
        connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
        cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
        cursor.execute("insert into müsterihesapkapatma(id,hesapid,hesaptürü) values(id,hesapid,hesaptürü)",(id,hesapid,hesaptürü))  #sorgu işlemi yapılır   
        connection.commit()#bağlatımızı ile imleç oluştuyoruz
        connection.close()#sorgumuzu kapaltık  
        
def hesapkapatma(id,hesapid,hesaptürü):# yeni bir fonksiyon oluşturduk
        connection=sqlite3.connect("admin.db")#veri tabanımıza bağlandık
        cursor=connection.cursor() #imleç oluşturması
        cursor.execute("SELECT id  hesapid hesaptürü FROM müsterihesapkapatma where id=? and hesapid=?  and hesaptürü=? ",(id,hesapid,hesaptürü))#müsterihesapkapatma datasına veri sorgulama işlemi yapılması
        result=cursor.fetchone()#verileri tek tek okuması
        if result:
            return True
        else:
            return False
def müsteriiban_db(id,hesaptürü,tc,müsiban,müsterikart):#burada  fonksiyon tanımlarım method atadık
        connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
        cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
        cursor.execute("insert into müsteriiban(id,hesaptürü,tc,müsiban,müsterikart) values(?,?,?,?,?)",(id,hesaptürü,tc,müsiban,müsterikart)) #sorgu işlemi yapılır   
        connection.commit()# bağlantımızı ile imleç oluşturmaası
        connection.close()#sorgumuzu kapatması
        
def iban(id,hesaptürü,tc,müsiban,müsterikart):# yeni bir fonksiyon oluşturduk
        connection=sqlite3.connect("admin.db")#veri tabanımıza bağlandık
        cursor=connection.cursor() #imleç oluşturması
        cursor.execute("SELECT id,hesaptürü,tc,müsiban,müsterikart  FROM müsteriiban where id=%s,  hesaptürü=%s , tc=? and müsiban=? and müsterikart=%s ",(id,hesaptürü,tc,müsiban,müsterikart))#müsteriiban datasını veri sorgulama işlemi yapılması 
        result=cursor.fetchone()#verileri tek tek okuması
        if result:
            return True
        else :
            return False    
                                 
            
def create_app(admin_db):#app  fonksiyon oluşturma
    conn=sqlite3.connect(admin_db)#admin db veri tabanını cağırması
    c=conn.cursor()#imleç oluşturması
    c.close()#veri kapatılması
  


    with app.app_context():
        admin_db()

    return app                    
        
        
def generate_report(year):
   format = request.args.get("format")

with app.test_request_context(
    "/make_report/2023", query_string={"format": "short"}
):
    generate_report(year=2023)
app=Flask(__name__)
app.secret_key = "super secret key"   # şifreleme işlemi yapara

con=sqlite3.connect("admin.db")
con.execute("CREATE TABLE IF NOT EXISTS müsteri('id integer primary key, numara numerıc,sifre numeric primary key,email Text,müsisim Text,dogumta numeric,cinsiyet BLOB')")
con.close()	 


@app.route("/")
def index():
        return render_template("view.html")# view sayfasını yönlendirir

    
@app.route("/sifre",methods=["POST","GET"])
def sifre():
        if request.method=="POST":
            id=request.form["id"] # veri okumak için id numra sifre eleştirme yapıyoruz
            numara=request.form["numara"]       
            sifre=request.form["sifre"]
            
            giris_admin_db(numara,sifre,id)# fonksiyonu çagrıypruz
            return redirect(url_for('index'))# index sayfasına yönlendirir
        
        else:
            return render_template("login.html")# sayfa hatalı ise login html yonlendilir
@app.route("/login")
def login():
        if request.method=="POST":
            numara=request.form["numara"]       
            sifre=request.form["sifre"]
            con=sqlite3.connect("admin.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("select * from müsteri where numara=? and sifre=?",(numara,sifre))
            giris=cur.fetchone()
            if giris:
                session["numara"]=numara#numara değeri giriniiyoz
                session["sifre"]=giris[sifre]
                return render_template("anasayfa.html",numara=numara)# numara aynı ise anasayfa yönlendirir
            else:
                sifre=request.form["sifre"]
                numara[numara]=sifre
                print(numara)
                redirect(url_for("index"))# yanlış ise index kısmına gönderir
                
@app.route("/login/anasayfa/")        
def anasayfa():    
        return render_template("anasayfa.html")#anasayfasına yönlendirmesi


@app.route("/login/anasayfa/ödemeler/faturaödeme",methods=["POST","GET"])#fatura ödeme ekranı
def faturaodeme():
        global id,müsterihesapno#method
        müsterihesapno="TR33 0006 1005 1978 6457 8413 26 "
        if request.method=="POST":#methodumuzu okur
            id=request.form["id"]#verimizi okumak için id,müsterihesapno eleştirmesi yapar
            müsterihesapno=request.form["müsterihesapno"]
        con=sqlite3.connect("admin.db")#veri tabanına bağlanması
        con.row_factory=sqlite3.Row#satır satır okuması
        cur=con.cursor()#imleç oluşturmasu
        cur.execute("SELECT  id FROM müsterifatura where id=? ",(id)).fetchall()#müsterifaturayı teker teker veriyi okuması
        fatura=cur.fetchone()[1]
        if fatura(id,müsterihesapno):
            session["id"]=id#id ve hesap no degeri girinir
            session["müsterihesapno"]=fatura[müsterihesapno]
            return render_template("fatura.html",id=id)#fatura.hmtl yönlerdirlir
        else:
            id=request.form["id"]
            müsterihesapno[müsterihesapno]=id
            redirect(url_for("anasayfa"))#yanlış girildiğinde anasayfaya yönlendilir
print(id)        
fatura(1,50000000)#fonksiyonu çalıştırma
   
@app.route("/login/anasayfa/ödemeler/İstanbulkart")#istanbul kart ekranı
def istanbulkart():
        global kartno,müsterihesapno#method
        if request.method=="POST":#methodumuzu okur
            id=request.form["id"]
            kartno=request.form["kartno"]#veriimizi okumak için  id,kartno,müsterihesapno eleştirmesi yapar
            müsterihesapno=request.form["müsterihesapno"]
            con=sqlite3.connect("admin.db")#veri tabanına bağlanması
            con.row_factory=sqlite3.Row#satır satır okuması
            cur=con.cursor()#imleç oluşturmasu
            cur.execute("SELECT * FROM müsteriistanbulkart where id=? , kartno=?  and müsterihesapno=? ",(id,kartno,müsterihesapno))#sorgu işlemi
            istanbulkart=cur.fetchone()#verileri tek tek okuması
        if istanbulkart:
            session["id"]=id
            session["kartno"]=kartno#id kartno müsterihesapno değeri giriniz
            session["müsterihesapno"]=müsterihesapno
            print(kartno,müsterihesapno)    
            return render_template("istanbulkart.html",kartno=kartno,id=id)#istanbulkart_html açılması
        else:
            redirect(url_for("anasayfa"))#anasayfaya yönlendirmesi    

    
@app.route("/login/anasayfa/iban transferleri")#iban ekranı
def iban(hesaptürü,tc,müsterikart):
     if request.method=="POST":#methodu okur
        id=request.form.get("id") # verilerini okumak için müsteriid,hesaptürü,tc,müsiban,müsterikart eleştirmesi yapar
        hesaptürü=request.form.get("hesaptürü")
        tc=request.form.get("tc")
        müsiban=request.form.get("müsiban")
        müsterikart=request.form.get("müsterikart")
        con=sqlite3.connect("admin.db")#vderi tabanına bağlanması
        con.row_factory=sqlite3.Row#satır satır okuması
        cur=con.cursor()#imleç oluşturması
        cur.execute("SELECT * FROM müsteriiban where id=? , hesaptürü=%s , tc=?  and müsterikart=? ",(id,hesaptürü,tc,müsiban,müsterikart))#sorgu işlemi yapılması        
        transfer=cur.fetchone() #iban fonksiyonu satır satır okuması
     if transfer(id,hesaptürü,tc,müsterikart):
        session["id"]=id
        session["hesaptürü"]=hesaptürü
        session["tc"]=tc# müsteriid,hesaptürü,tc,müsiban,müsterikart bilgileri giriniz
        session["müsiban"]=müsiban
        session["müsterikart"]=müsterikart
        flash('bilgileri giriniz')
        return render_template("paratransfer.html",id=id,hesaptürü=hesaptürü,tc=tc,müsterikart=müsterikart)#paratransfer_html ekranına geçilmesi
     else:
            id=request.form["id"]
            müsiban[müsiban]=id#müsiban ile id eleşmesşsi
            print(müsiban)
            redirect(url_for("anasayfa"))#anasayfa ekranına geçilmesi
           
 
@app.errorhandler(404)
def not_found():
    """Page not found."""#hata try-catch işlemi
    return (render_template("404.html"), 404)
@app.route('/login/anasayfa/digerislemler/kredi başvuru')# kredi başvuru ekranı
def kredi():
        if request.form=="POST":#method okur
          id=request.form["id"]# verileri okumak için id,tutar,hesap eleştirmesi yapar
          tutar=request.form["tutar"]
          hesap=request.form["hesap"]
        con=sqlite3.connect("admin.db")# vertabanına bağlar
        con.row_factory=sqlite3.Row#satırları okumasını sağlar
        cur=con.cursor()#imleç oluşturur
        cur.execute("SELECT  id,tutar,hesap FROM müsterikredibaşvuru  where id=?,tutar=? and hesap=?",(id,tutar,hesap))#sorgu işlemi
        if kredi:
            session["id"]=id#id ,tutar hesap bilgileri girilmesi
            session["tutar"]=tutar
            session["hesap"]=hesap
            return render_template("kredi.html",id=id,tutar=tutar,hesap=hesap)#kredi.html sayfasına yönlendilir
        else:
            id=request.form["id"]
            hesap[hesap]=id#hesap id eleştirmesi yapılması
            print(hesap)
            redirect(url_for("anasayfa"))#anasayfa ekranına geçilmesi 
@app.route("/login/anasayfa/limitvebakiye/")
def limit():
    return render_template("limit.html")#limit bakiye ekranına geçilir                 
@app.route("/login/anasayfa/limitvebakiye/hesapacma")#hesapaçma ekranı
def hesap():
        if request.form=="POST":#methodu okur
           id=request.form["id"]#verileri okumak için id,hesapid,hesaptürü eleştirmesi yapar
           hesapid=request.form["hesapid"]
           hesaptürü=request.form["hesaptürü"]
        con=sqlite3.connect("admin.db")#veri tabanına bağlanır
        con.row_factory=sqlite3.Row#satrıarı okur
        cur=con.cursor()#imleç oluştulur
        cur.execute("SELECT id,hesapid,hesaptürü FROM müsterihesapacma where id=?,hesapid=? and hesaptürü=?",(id,hesapid,hesaptürü))#sorgu işlemi yapar
            
        if hesap:
            session["id"]=id #id,hesapid,hesaptürü bilgileri girillir
            session["hesapid"]=hesapid
            session["hesaptürü"]=hesaptürü
            return render_template("hesapacma.html",id=id,hesapid=hesapid,hesaptürü=hesaptürü)# hesapacma_html geçilr
        else:
            id=request.form["id"]
            hesaptürü[hesaptürü]=id#hesaptürü ile id eleştirmesi yapılır
            print(hesaptürü)
            redirect(url_for("anasayfa"))#anasayfa ekranına geçilir
@app.route("/login/anasayfa/limitvebakiye/hesap kapatma")#hesap kapatma ekranı
def hesapkapatma():
        if request.form=="POST":#methodu okur
             id=request.form["id"]
             hesapid=request.form["hesapid"]#verileri okumak için id,hesapid,hesaptürü eleştirmesi yapar
             hesaptürü=request.form["hesaptürü"]
           
        con=sqlite3.connect("admin.db")#veri tabanına bağlanır
        con.row_factory=sqlite3.Row#satrıarı okur
        cur=con.cursor()#imleç oluştulur
        cur.execute("SELECT id,hesapid,hesaptürü FROM müsterihesapkapatma where id=?,hesapid=? and hesaptürü=?",(id,hesapid,hesaptürü))#sorgu işlemi
        if hesapkapatma:
            session["id"]=id
            session["hesapid"]=hesapid#id,hesapid,hesaptürü bilgileri girillir
            session["hesaptürü"]=hesaptürü
            return render_template("hesapkapatma.html",id=id,hesapid=hesapid,hesaptürü=hesaptürü)#hesapkapatma_html geçilmesi
        else:
            id=request.form["id"]
            hesaptürü[hesaptürü]=id#hesaptürü ile id eleştirme yapılır
            print(hesaptürü)
            redirect(url_for("anasayfa"))#anasayfa ekranına geçilmesi
@app.route("/login/anasayfa/digerislemler/para çekme")#para çekme ekranı
def çekme():
        if request.method=="POST":# methodu okur
           id=request.form["id"]#verileri okumak için id,kartid,tutar eleştirmesi yapar
           kartid=request.form["kartid"]
           tutar=request.form["tutar"]
        con=sqlite3.connect("admin.db")#veri tabanı bağlanması
        con.row_factory=sqlite3.Row#satırları okur
        cur=con.cursor()#imleç oluşturulur
        cur.execute("SELECT * FROM müsteriparacekme where id=? and kartid=?  and tutar=? ",(id,kartid,tutar))#sorgu işlemi
        if cekme:
            session["id"]=id#müsid,kartid,tutar bilgileri girilir
            session["kartid"]=kartid
            session["tutar"]=tutar
            islem=input("işlem yapmak için numarayı giriniz")#numarayo girir
            if(islem=="q"):
                print("işlemden çıkılır")
            elif (islem=="4"):
                miktar=int(input("miktar giriniz"))
                if(tutar-miktar<0):
                    print("yetersiz bakiye")
        
                else:
                    tutar=tutar-miktar
                    print("hesabınızdan {} tl para çektiniz".format(miktar))         
                    müsid=request.form["müsid"]
                    kartid[kartid]=müsid
                    print(kartid)        
        
            return render_template("para çekme.html",müsid=müsid,kartid=kartid,tutar=tutar)#para çekilme ekranıma geçilir
        else:
            redirect(url_for("anasayfa"))#anasayfa ya yönlendilir

@app.route("/login/anasayfa/digerislemler/para yatırma")#para yatırma ekranı
def yatırma():
       if request.method=="POST":#methodu okuma
            id=request.form["id"]
            hesapid=request.form["hesapid"]#verileri okumak için müsid,limit,hesapid eleştirmesi yapar
            limit=request.form["limit"]
            con=sqlite3.connect("admin.db")#veri tabanına girilmesi
            con.row_factory=sqlite3.Row#satırları okur
            cur=con.cursor()#imleç oluşturulur
            cur.execute("SELECT * FROM müsteriparayatırma where id=? ,hesapid=?  and limit=? ",(id,hesapid,limit))#sorgu işlemi yapılması
            if yatırma:
                session["id"]=id# müsid,hesapid,limit bilgileri girilmesi
                session["hesapid"]=hesapid
                session["limit"]=limit
                islem=input("işlem yapmak için numarayı giriniz")
                if(islem=="q"):
                    print("ana sayfa'ya döner")
                elif(islem=="5"):
                 yatacak=int(input("yatırmak olan tutar girin"))
                limit=limit-yatacak
                print("hesabınıza {} tl yatırdı".format(yatacak)) 
                
                    
            return render_template("para yatırma.html",id=id,hesapid=hesapid,limit=limit)#para yatırma ekranına geçilmes
       else:
           return(redirect(url_for("anasayfa")))#anasayfa ekranına geçilmesi
            
@app.route("/login/anasayfa/cıkıs")#çıkış ekranı
def cıkıs():
        session.clear()
        return render_template("çıkış.html")
if __name__ == "__main__":    app.run(debug=True)

cekme(1,20000000000,500)
parayatırma(1,200000,500000)
hesapacma(1,1,"vadesiz tl hesap")
hesapkapatma(1,1,"vadesiz dolar hesap")
kredi()#fonksiyonları çağırması
exit()
