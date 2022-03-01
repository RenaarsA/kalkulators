from ast import operator
from distutils import command
import numbers
from tkinter import*
from math import*
from unittest import result

mansLogs=Tk()
mansLogs.title('Kalkulators')


def btnClick(number):
    current=e.get() #nolasa esošo skaitli
    e.delete(0,END) #nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) #ievieto displejā
    return 0

def btnCommand(command):
    global number
    global num1 #jāiegaumē skaitlis un darbība
    global mathOp #matemātisks operātors
    mathOp=command #+,-,*,/
    num1=float(e.get())
    e.delete(0,END)
    return 0

def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=='+':
        result=num1+num2
    elif mathOp=='-':
        result=num1-num2
    elif mathOp=='*':
        result=num1*num2
    elif mathOp=='/':
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0
def pi():

    if mathOp=='π':
        result=pi
    return result

def sq_rt():
    global operator
    global num1
    global mathOp
    mathOp=command
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    result

def kvad():
    global operator
    global num1
    global mathOp
    mathOp=command
    num1=(float(e.get())**2)
    e.delete(0,END)
    e.insert(0,num1)
    result

def min():
    global operator
    global mathOp #matemātiskais operators
    global num1
    num1=-(float(e.get()))
    e.delete(0,END)
    e.insert(0,str(num1))
    return 0


def notirit():
    e.delete(0,END)
    num1=0
    mathOp=''
    return 0



e=Entry(mansLogs,width=15,bd=20,font=('Arial Black',20))
btn0=Button(mansLogs,text='0',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(0))
btn1=Button(mansLogs,text='1',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(1))
btn2=Button(mansLogs,text='2',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(2))
btn3=Button(mansLogs,text='3',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(3))
btn4=Button(mansLogs,text='4',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(4))
btn5=Button(mansLogs,text='5',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(5))
btn6=Button(mansLogs,text='6',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(6))
btn7=Button(mansLogs,text='7',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(7))
btn8=Button(mansLogs,text='8',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(8))
btn9=Button(mansLogs,text='9',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnClick(9))
btnreiz=Button(mansLogs,text='*',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnCommand('*'))
btndali=Button(mansLogs,text='/',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnCommand('/'))
btnpiesk=Button(mansLogs,text='+',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnCommand('+'))
btnatnem=Button(mansLogs,text='-',bd=20,font=('Arial Black',20),padx='40',pady='20',command=lambda:btnCommand('-'))
btnVien=Button(mansLogs,text='=',bd=20,font=('Arial Black',20),padx='40',pady='20',command=vienads)
btnDzest=Button(mansLogs,text='C',bd=20,font=('Arial Black',20),padx='40',pady='20',command=notirit)
btnkoma=Button(mansLogs,text=',',bd=20,font=('Arial Black',20),padx='45',pady='20',command=lambda:btnCommand('.'))
btnkvad=Button(mansLogs,text='x²',bd=20,font=('Arial Black',20),padx='37',pady='20',command=kvad)
btnproc=Button(mansLogs,text='√',bd=20,font=('Arial Black',20),padx='40',pady='20',command=sq_rt)
btnpi=Button(mansLogs,text='+/-',bd=20,font=('Arial Black',20),padx='31',pady='20',command=min)

e.grid(row=0,column=0,columnspan=4)

btnDzest.grid(row=1,column=0)
btnkvad.grid(row=1,column=1)
btnproc.grid(row=1,column=2)
btndali.grid(row=1,column=3)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnreiz.grid(row=2,column=3)



btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnatnem.grid(row=3,column=3)


btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnpiesk.grid(row=4,column=3)

btnpi.grid(row=5,column=0)
btn0.grid(row=5,column=1)
btnkoma.grid(row=5,column=2)
btnVien.grid(row=5,column=3)






mansLogs.mainloop()