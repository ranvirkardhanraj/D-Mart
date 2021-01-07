from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
con = pymysql.connect(host="db4free.net", database="feedback_dhanraj", user="dhanrajranvirkar", password="Dhanraj@007.com",port=3306 )
base1=Tk()
base1.geometry("650x550")
base1.title("Worker Product System")

def addproduct():
    blanklabel = Label(base1, text="", bg="white", width=89, height=25)
    blanklabel.place(x=10, y=120)
    namel=Label(base1,text="Name",font=("Arial Bold",12),bg="white")
    namel.place(x=15,y=130)
    namel = Label(base1, text="Cost", font=("Arial Bold", 12), bg="white")
    namel.place(x=300, y=130)
    namel = Label(base1, text="Type", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=160)
    namel = Label(base1, text="Total Cost", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=220)
    namel = Label(base1, text="Quantity", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=190)
    namel = Label(base1, text="Size", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=250)
    namel = Label(base1, text="Brand", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=280)
    namel = Label(base1, text="Date", font=("Arial Bold", 12), bg="white")
    namel.place(x=15, y=310)
    pnameen=Entry(base1)
    pnameen.place(x=120,y=130)
    ptypeen=Entry(base1)
    ptypeen.place(x=120,y=160)
    pmaincost=Entry(base1)
    pmaincost.place(x=390,y=130)
    pcosten=Entry(base1)
    def totalc(event):
        maincost = int(pmaincost.get())
        quantity = int(pquantityen.get())
        total = maincost * quantity
        pcosten.insert(0,total)
    pcosten.bind("<FocusIn>",totalc)
    pcosten.place(x=120,y=220)
    pquantityen=Entry(base1)
    pquantityen.place(x=120,y=190)

    psizeen=Entry(base1)
    psizeen.place(x=120,y=250)
    pbranden=Entry(base1)
    pbranden.place(x=120,y=280)
    pdateen=Entry(base1)
    pdateen.place(x=120,y=310)

    def addp():
        pname=pnameen.get()
        pmcost=pmaincost.get()
        ptype=ptypeen.get()
        pquantity = pquantityen.get()
        ptcost=pcosten.get()
        psize=psizeen.get()
        pbrand=pbranden.get()
        pdate=pdateen.get()
        quary="insert into products value('"+pname+"',"+pmcost+",'"+ptype+"',"+pquantity+","+ptcost+",'"+psize+"','"+pbrand+"','"+pdate+"')"
        cur=con.cursor()
        cur.execute(quary)
        con.commit()
        cur.close()

        pnameen.delete(0,END)
        pmaincost.delete(0,END)
        ptypeen.delete(0,END)
        pquantityen.delete(0,END)
        pcosten.delete(0,END)
        psizeen.delete(0,END)
        pbranden.delete(0,END)
        pdateen.delete(0,END)
        messagebox.askquestion("message","Are you sure")
        messagebox.showinfo("Message","Data Saved")
    addb=Button(base1,text="ADD",font=("Arial Bold",12),bg="yellow",width=12,command=addp)
    addb.place(x=15,y=350)


workeraddb=Button(base1,text="ADD Product",bg="white",command=addproduct)
def addcolor(event):
    workeraddb.configure(bg="red")
workeraddb.bind("<Enter>",addcolor)
def adddecolor(event):
    workeraddb.configure(bg="white")
workeraddb.bind("<Leave>",adddecolor)
workeraddb.place(x=1,y=1)

def productdeb():
    blanklabel = Label(base1, text="", bg="white", width=89, height=25)
    blanklabel.place(x=10, y=120)
    def lista(event):
        namep=lisb.selection_get()
        quary2 = "select cost,type,quantity,totalcost,size,brand,date from products where name='"+namep+"'"
        cur = con.cursor()
        cur.execute(quary2)
        data=cur.fetchone()
        cur.close()
        llcost.config(text=data[0])
        lltype.config(text=data[1])
        llquantity.config(text=data[2])
        lltotalc.config(text=data[3])
        llsize.config(text=data[4])
        llbrand.config(text=data[5])
        lldate.config(text=data[6])

    lisb=Listbox(base1,selectmode=SINGLE)
    lisb.bind("<ButtonRelease>",lista)
    lisb.place(x=20,y=140)
    quary="select name from products"
    cur=con.cursor()
    cur.execute(quary)
    data=cur.fetchall()
    i=0
    for d1 in data:
        for d2 in d1:
            lisb.insert(i,d2)
            i=i+1
    cur.close()


    lcost=Label(base1,text="Cost:",font=("Arial Bold",12),bg="white")
    lcost.place(x=170,y=140)
    ltype=Label(base1,text="Type",font=("Arial Bold",12),bg="white")
    ltype.place(x=170,y=170)
    lquantity=Label(base1,text="Quantity:",font=("Arial Bold",12),bg="white")
    lquantity.place(x=170,y=200)
    ltotalc=Label(base1,text="Total Cost:",font=("Arial Bold",12),bg="white")
    ltotalc.place(x=170,y=230)
    lsize=Label(base1,text="Size:",font=("Arial Bold",12),bg="white")
    lsize.place(x=170,y=260)
    lbrand=Label(base1,text="Brand:",font=("Arial Bold",12),bg="white")
    lbrand.place(x=170,y=290)
    ldate=Label(base1,text="Date",font=("Arial Bold",12),bg="white")
    ldate.place(x=170,y=320)
    llcost=Label(base1,text="",font=("Arial Bold",12),bg="white")
    llcost.place(x=270,y=140)
    lltype=Label(base1,text="",font=("Arial Bold",12),bg="white")
    lltype.place(x=270,y=170)
    llquantity=Label(base1,text="",font=("Arial Bold",12),bg="white")
    llquantity.place(x=270,y=200)
    lltotalc=Label(base1,text="",font=("Arial Bold",12),bg="white")
    lltotalc.place(x=270,y=230)
    llsize=Label(base1,text="",font=("Arial Bold",12),bg="white")
    llsize.place(x=270,y=260)
    llbrand=Label(base1,text="",font=("Arial Bold",12),bg="white")
    llbrand.place(x=270,y=290)
    lldate=Label(base1,text="",font=("Arial Bold",12),bg="white")
    lldate.place(x=270,y=320)
allwokerdetailsb=Button(base1,text="Details",bg="white",command=productdeb)

def allworkercolor(event):
    allwokerdetailsb.configure(bg="red")
allwokerdetailsb.bind("<Enter>",allworkercolor)

def allworkerde(event):
    allwokerdetailsb.configure(bg="white")
allwokerdetailsb.bind("<Leave>",allworkerde)
allwokerdetailsb.place(x=75,y=1)

def productsearch():
    blanklabel = Label(base1, text="", bg="white", width=89, height=25)
    blanklabel.place(x=10, y=120)
    pnamel=Label(base1,text="Enter Product Name:",font=("Arial Bold",12),bg="white")
    pnamel.place(x=20,y=130)
    pnameen=Entry(base1)
    pnameen.place(x=200,y=130)
    pnamel = Label(base1, text="Enter Product Type:", font=("Arial Bold", 12), bg="white")
    pnamel.place(x=20, y=160)
    ptypeen=Entry(base1)
    ptypeen.place(x=200,y=160)
    pcost=Label(base1,text="Cost", font=("Arial Bold", 12), bg="white")
    pcost.place(x=20,y=290)
    pquantity=Label(base1,text="Quantity", font=("Arial Bold", 12), bg="white")
    pquantity.place(x=100,y=290)
    totalc=Label(base1,text="Total Cost", font=("Arial Bold", 12), bg="white")
    totalc.place(x=200,y=290)
    size=Label(base1,text="Size", font=("Arial Bold", 12), bg="white")
    size.place(x=310,y=290)
    brand=Label(base1,text="Brand", font=("Arial Bold", 12), bg="white")
    brand.place(x=400,y=290)
    date=Label(base1,text="Date", font=("Arial Bold", 12), bg="white")
    date.place(x=20,y=340)
    def searchp():
        productname=pnameen.get()
        ptype=ptypeen.get()
        quary="select cost,quantity,totalcost,size,brand,date from products where (name ='"+productname+"' AND type='"+ptype+"')"
        cur=con.cursor()
        cur.execute(quary)
        data=cur.fetchone()
        cur.close()
        if data==None:
            messagebox.showerror("Error","there is no product of name='"+productname+"' of type='"+ptype+"'")
            pnameen.delete(0,END)
            ptypeen.delete(0,END)
        else:
            pcost.config(text=data[0])
            pquantity.config(text=data[1])
            totalc.config(text=data[2])
            size.config(text=data[3])
            brand.config(text=data[4])
            date.config(text=data[5])


    searchb=Button(base1,text="Search",font=("Arial Bold",12),bg="yellow",fg="red",command=searchp)
    searchb.place(x=20,y=190)
searchworkerb=Button(base1,text="Search",bg="white",command=productsearch)
def deleitm():
    blanklabel = Label(base1, text="", bg="white", width=89, height=25)
    blanklabel.place(x=10, y=120)
    labelname=Label(base1,text="Enter a Name of item:",font=("Arial Bold",12),bg="white")
    labelname.place(x=20,y=130)
    labeltype=Label(base1,text="Enter Type of item:",font=("Arial Bold",12),bg="white")
    labeltype.place(x=20,y=160)
    nameentry=Entry(base1)
    nameentry.place(x=230,y=130)
    typeentry=Entry(base1)
    typeentry.place(x=230,y=160)
    sizelabel=Label(base1,text="Enter size of Item:",font=("Arial Bold",12),bg="white")
    sizelabel.place(x=20,y=190)
    sizeentry=Entry(base1)
    sizeentry.place(x=230,y=190)
    def deleitem():
        quary = "select * from products"
        cur = con.cursor()
        cur.execute(quary)
        data = cur.fetchall()
        cur.close()
        listdata=[]

        for d1 in data:
            for d2 in d1:
                listdata.append(d2)
        pname = nameentry.get()
        ptype = typeentry.get()
        psize = sizeentry.get()
        if listdata.__contains__(pname and ptype and psize):
            quary2="DELETE from products where (name='"+pname+"')"
            cur=con.cursor()
            cur.execute(quary2)
            con.commit()
            cur.close()
            messagebox.showinfo("Message","Product of name is '"+pname+"' deleted ")
            nameentry.delete(0,END)
            typeentry.delete(0,END)
            sizeentry.delete(0,END)
        else:
            messagebox.showerror("message","No such a product of name is '"+pname+"'")
    delebutton=Button(base1,text="Delete",font=("Arial Bold",12),bg="white",command=deleitem,fg="red")
    delebutton.place(x=20,y=230)


deleteitem=Button(base1,text="Delete",command=deleitm,bg="white")
def colorred(event):
    deleteitem.configure(bg="red")
deleteitem.bind("<Enter>",colorred)
def whitecolor(event):
    deleteitem.configure(bg="white")
deleteitem.bind("<Leave>",whitecolor)
deleteitem.place(x=162,y=1)
def searworkcolor(event):
    searchworkerb.configure(bg="red")
searchworkerb.bind("<Enter>",searworkcolor)

def searworkdecolor(event):
    searchworkerb.configure(bg="white")
searchworkerb.bind("<Leave>",searworkdecolor)
searchworkerb.place(x=119,y=1)

def exited():
    con.close()
    exit(0)
exitb=Button(base1,text="Exit",bg="white",command=exited,fg="blue",width=14,font=("Arial Bold",12))
def allworkercolor(event):
    exitb.configure(bg="red")
exitb.bind("<Enter>",allworkercolor)

def allworkerde(event):
    exitb.configure(bg="white")
exitb.bind("<Leave>",allworkerde)
exitb.place(x=500,y=1)

headline1=Label(base1,text="Products Management System",font=("Arial Bold",12),fg="green")
headline1.place(x=190,y=50)
headline2=Label(base1,text="Select Above Button",font=("Arial Bold",8),fg="green")
headline2.place(x=230,y=80)
base1.mainloop()