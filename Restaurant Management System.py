from tkinter import*
import random
import time
import datetime
from fpdf import FPDF

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#Adding date & time
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('Arial',60,'bold'),text="FOOD JUNCTION",fg="Navy",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('Arial',20,'bold'),text=localtime,fg="Navy",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#generating reference number
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
#calculating bill amount
    if (Fries.get()==""):
        CoFries=0
    else:
        CoFries=float(Fries.get())


    
    if (Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())



    if (Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())



    if (Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

        
    if (Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofFries =CoFries * 40
    CostofDrinks=CoD * 65
    CostofNoodles = CoNoodles* 90
    CostofSoup = CoSoup * 55
    CostBurger = CoBurger* 60
    CostSandwich=CoSandwich * 80

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))

    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich) * 0.2)

    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)
 
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost) 
#bill creation  
    pdf = FPDF(orientation ='P',unit ='mm',format ='A4') 
    pdf.add_page()
    pdf.set_margins(13,0,8)
#font style and size
    pdf.set_font("Arial", size = 20)
#creating cells and adding values into cell
    pdf.cell(200, 10, txt ="FOOD JUNCTION",ln = 1, align = 'C')
    pdf.ln(4)
    pdf.set_font("Arial", size = 14)
    pdf.cell(180, 5, txt ="DINE IN-INVOICE NO:"+randomRef,border='B',ln = 1, align = 'L') 

    if(CoFries!=0):
        pdf.cell(200,10,txt="Fries: "+"40 x "+str(int(CoFries))+"="+"RS."+str(CostofFries),ln=2,align='L')
    if(CoD!=0):
        pdf.cell(200,10,txt="Drinks: "+"65 x "+str(int(CoD))+"="+"RS."+str(CostofDrinks),ln=2,align='L')
    if(CoNoodles!=0):
        pdf.cell(200,10,txt="Noodles: "+"90 x "+str(int(CoNoodles))+"="+"RS."+str(CostofNoodles),ln=2,align='L')
    if(CoSoup!=0):
        pdf.cell(200,10,txt="Soups: "+"55 x "+str(int(CoSoup))+"="+"RS."+str(CostofSoup),ln=2,align='L')
    if(CoBurger!=0):
        pdf.cell(200,10,txt="Burgers: "+"60 x "+str(int(CoBurger))+"="+"RS."+str(CostBurger),ln=2,align='L')    
    if(CoSandwich!=0):
        pdf.cell(200,10,txt="Sandwichs: "+"80 x "+str(int(CoSandwich))+"="+"RS."+str(CostSandwich),ln=2,align='L')

    pdf.cell(180, 5, txt ="Cost of Meal: "+"RS."+str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich)),ln = 1, align = 'R')
    pdf.cell(180,3,txt="",border='T',ln=1,align='L')
    pdf.cell(180, 5, txt ="Sub Total: "+"RS."+str(str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))),ln = 1, align = 'R')
    pdf.cell(180, 5, txt ="Service Charge: "+"RS."+str('%.2f' % Ser_Charge),ln = 1, align = 'R')
    pdf.cell(180, 5, txt ="State Tax: "+"RS."+str('%.2f' % PayTax),ln = 1, align = 'R')
    pdf.cell(180,3,txt="",border='T',ln=1,align='L')
    pdf.cell(180, 5, txt ="Total Cost: "+"RS."+str('%.2f' % (PayTax+TotalCost+Ser_Charge)),ln = 0, align = 'R')
    
#saving the bill in pdf format
    pdf.output("BILL "+str(randomRef)+".pdf")  
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    
#creating labels and textboxes(design 1)
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="BILL ID",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="FRIES",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="NOODLES",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="SOUP",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="BURGER",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="SANDWICH",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)

#creating labels and textboxes(design 2)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="DRINKS",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="COST OF MEAL",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="SERVICE CHARGE",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="STATE TAX",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="SUB TOTAL",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="TOTAL COST",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#creating buttons(design 3)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="TOTAL",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="RESET",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="EXIT",bg="powder blue",command=qExit).grid(row=7,column=3)

#run application

root.mainloop()


