from flask import Flask,render_template,url_for,request,redirect,flash,session# kütüphaneler
import sqlite3 # veri tabanını dahil ettik
                   
def giris_admin_db(numara,sifre,id): #burada  fonksiyon tanımlarım method atadık
       connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
       cursor=connection.cursor() #bağlatımızı ile imleç oluştuyoruz
       cursor.execute("insert into müsteri(id,numara,sifre) values(?,?,?)",(sifre,numara,id)) # sorgu işlemi
       connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
       connection.close()# sorgumuzu kapattık
def giris(numara,sifre,id):#yeni bir fonkisyon oluşturuyoruz
        connection=sqlite3.connect("admin.db")# burada veri tabanına bağlandık
        cursor=connection.cursor()#bağlatımızı ile imleç oluştuyoruz
        cursor.execute('SELECT numara sifre FROM müsteri WHERE numara=? and sifre=? and id=?',(numara,sifre,id))# sorgu işlemi    
        result=cursor.fetchone()# verileri tek tek okumayı sağlar
        if result:
         return True
        else:
            return False
def müsterifatura_db(müsteriid,müsterihesapno):#burada  fonksiyon tanımlarım method atadık
     connection=sqlite3.connect("admin.db")# burada veri tabanımıza bağlandık
     cursor=connection.cursor()#imleç işlemini yapıyoruz
     cursor.execute("insert into müsterifatura(müsteriid,müsterihesapno) values(?,?)",(müsteriid,müsterihesapno))# imleç yolu ile sorgu işlemi yapıyoruz
     connection.commit()#yapıtıgımız işlemi veri tabanı işlenmesi
     connection.close()# sorgumuzu kapattık
def fatura (müsteriid,müsterihesapno):
     connection=sqlite3.connect("admin.db")# veri tabanına bağlanması
     cursor=connection.cursor()#imleç oluştuyoruz
     cursor.execute('SELECT müsterid müsterihesapno FROM müsterifatura where müsteriid=? and müsterihesapno=? ',(müsteriid,müsterihesapno))#müşterifatura datamızın sorgu işlemini yapılır    
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
        cursor.execute("SELECT id,hesaptürü,tc,müsiban,müsterikart  FROM müsteriiban where müsterid=%s,  hesaptürü=%s , tc=? and müsiban=? and müsterikart=%s ",(id,hesaptürü,tc,müsiban,müsterikart))#müsteriiban datasını veri sorgulama işlemi yapılması 
        result=cursor.fetchone()#verileri tek tek okuması
        if result:
            return True
        else :
            return False            
app=Flask(__name__)
app.secret_key = '123'# şifreleme işlemi yapara

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
        if request.method=="POST":#methodumuzu okur
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
@app.route("/login/anasayfa/ödemeler/faturaödeme")#fatura ödeme ekranı
def faturaodeme(müsteriid,müsterihesapno):
        if request.method=="POST":#methodumuzu okur
            müsteriid=request.form["müsteriid"] #verimizi okumak için id,müsterihesapno eleştirmesi yapar
            müsterihesapno=request.form["müsterihesapno"]
        con=sqlite3.connect("admin.db")#veri tabanına bağlanır
        con.row_factory=sqlite3.Row#satırları dönmesini sağlar
        cur=con.cursor()#imleç
        cur.execute("SELECT * FROM müsterifatura where müsteriid =? and müsteri hesap no=? ",(müsteriid,müsterihesapno))#sorgu işlemi yapar
        fatura=cur.fetchone()#tek tek okur
        if fatura:
            session["müsteriid"]=müsteriid#id ve hesap no degeri girinir
            session["müsterihesapno"]=fatura[müsterihesapno]
            return render_template("fatura.html",müsteriid=müsteriid,müsterihesapno=müsterihesapno)#fatura.hmtl yönlerdirlir
        else:
            redirect(url_for("anasayfa"))#anasayfa ya yönderdilir
    
@app.route("/login/anasayfa/ödemeler/İstanbulkart")#istanbulkart ekranı
def istanbulkart():
        if request.method=="POST":#methodumuzu okur
            id=request.form["id"]
            kartno=request.form["kartno"]#veriimizi okumak için  id,kartno,müsterihesapno eleştirmesi yapar
            müsterihesapno=request.form["müsterihesapno"]
            con=sqlite3.connect("admin.db")#veri tabanına bağlanır
            con.row_factory=sqlite3.Row#satırları dönmesini sağlar
            cur=con.cursor()#imle. oluşturulur
            cur.execute("SELECT * FROM müsteriistanbulkart where id=? , kartno=?  and müsterihesapno=? ",(id,kartno,müsterihesapno))#sorgu işlemi
            istanbulkart=cur.fetchone()#verileri tek tek okur
        if istanbulkart:
            session["id"]=id#id kartno müsterihesapno değeri giriniz
            session["kartno"]=kartno
            session["müsterihesapno"]=müsterihesapno    
            return render_template("istanbulkart.html",kartno=kartno,id=id)#istanbulkart_html yönlendiliri
        else:
            redirect(url_for("anasayfa"))    #anasayfaya yönlerdilir
    
@app.route("/login/anasayfa/iban transferleri")#iban ekranı
def iban():
     if request.method=="POST":#methodu okur
        id=request.form["id"] # verilerini okumak için müsteriid,hesaptürü,tc,müsiban,müsterikart eleştirmesi yapar
        hesaptürü=request.form["hesaptürü"]
        tc=request.form["tc"]
        müsiban=request.form["müsiban"]
        müsterikart=request.form["müsterikart"]
        con=sqlite3.connect("admin.db")#veritabanı bağlar
        con.row_factory=sqlite3.Row#satırları okumasını sağlar
        cur=con.cursor()#imleç işlmemi yapar
        cur.execute("SELECT * FROM müsteriiban where id=? , hesaptürü=%s , tc=? , müsiban=? and müsterikart=? ",(id,hesaptürü,tc,müsiban,müsterikart)) #sorgu işlemi yapar       
     if iban:
        session["id"]=id
        session["hesaptürü"]=hesaptürü
        session["tc"]=tc# müsteriid,hesaptürü,tc,müsiban,müsterikart bilgileri giriniz
        session["müsiban"]=müsiban
        session["müsterikart"]=müsterikart
        return render_template("paratransfer.html",id=id,hesaptürü=hesaptürü,tc=tc,müsiban=müsiban,müsterikart=müsterikart)#para_transferhtml yönlerdilir
     else:
         redirect(url_for("anasayfa"))# anasayfaya yönlerdilir
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
            redirect(url_for("anasayfa"))      #anasayfaya yönlendirlr
@app.route("/login/anasayfa/limitvebakiye/hesapacma") #hesapacma ekranı
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
            redirect(url_for("anasayfa"))#anasayfa geçilir
@app.route("/login/anasayfa/limitvebakiye/hesap kapatma")#hesapkapatma ekranı
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
            redirect(url_for("anasayfa"))#anasayfa
@app.route("/login/anasayfa/digerislemler/para çekme")#para çekme ekranı 
def çekme():
        if request.method=="POST":# methodu okur
           müsid=request.form["müsid"]#verileri okumak için müsid,kartid,tutar eleştirmesi yapar
           kartid=request.form["kartid"]
           tutar=request.form["tutar"]
        con=sqlite3.connect("admin.db")#veri tabanı bağlanması
        con.row_factory=sqlite3.Row#satırları okur
        cur=con.cursor()#imleç oluşturulur
        cur.execute("SELECT * FROM müsteriparacekme where müsid=? and kartid=?  and tutar=? ",(müsid,kartid,tutar))#sorgu işlemi
        if cekme:
            session["müsid"]=müsid#müsid,kartid,tutar bilgileri girilir
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
                
        
        return render_template("para çekme.html",müsid=müsid,kartid=kartid,tutar=tutar)#paraçekme_html yönlendilir
@app.route("/login/anasayfa/digerislemler/para yatırma")#para yatırma ekranı
def yatırma():
        if request.method=="POST":#methodu okuma
            müsid=request.form["müsid"]
            hesapid=request.form["hesapid"]#verileri okumak için müsid,limit,hesapid eleştirmesi yapar
            limit=request.form["limit"]
            con=sqlite3.connect("admin.db")#veri tabanına girilmesi
            con.row_factory=sqlite3.Row#satırları okur
            cur=con.cursor()#imleç oluşturulur
            cur.execute("SELECT * FROM müsteriparayatırma where müsid=? ,hesapid=?  and limit=? ",(müsid,hesapid,limit))#sorgu işlemi yapılması
            if yatırma:
                session["müsid"]=müsid# müsid,hesapid,limit bilgileri girilmesi
                session["hesapid"]=hesapid
                session["limit"]=limit
                islem=input("işlem yapmak için numarayı giriniz")
                if(islem=="q"):
                    print("ana sayfa'ya döner")
                elif(islem=="5"):
                 yatacak=int(input("yatırmak olan tutar girin"))
                limit=limit-yatacak
                print("hesabınıza {} tl yatırdı".format(yatacak)) 
                
                    
        return render_template("para yatırma.html",müsid=müsid,hesapid=hesapid,limit=limit)#parayatırma_html ekranına geçilmesi
@app.route("/login/anasayfa/cıkıs")
def cıkıs():
        session.clear()
        return render_template("çıkış.html")