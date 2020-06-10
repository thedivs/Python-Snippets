

# Author : DIVS TECH

from tkinter import *
top = Tk()
top.title("Calculator")
top.iconbitmap('cal.ico')

def click(number):
	global oprator
	oprator = oprator + str(number)
	variable.set(oprator)
def clear():
	global oprator
	oprator = ""
	variable.set(oprator)
def sum():
	global oprator
	oprator = str(eval(oprator))
	variable.set(oprator)
def quit():
	exit()
oprator = ""

variable = StringVar()
display = Entry(top,bd=5,textvariable=variable,justify="right")
display.grid(columnspan=6)

btn1=Button(top,text="1",bd=5,padx=15,command=lambda:click(1))
btn1.grid(row=3,column=0)

btn2=Button(top,text="2",bd=5,padx=15,command=lambda:click(2))
btn2.grid(row=3,column=1)

btn3=Button(top,text="3",bd=5,padx=15,command=lambda:click(3))
btn3.grid(row=3,column=2)

btn0=Button(top,text="0",bd=5,padx=15,command=lambda:click(0))
btn0.grid(row=4,column=0)

btnpoint=Button(top,text=".",bd=5,padx=15,command=lambda:click("."))
btnpoint.grid(row=4,column=1)

btnclear=Button(top,text="C",bd=5,padx=15,command=clear)
btnclear.grid(row=4,column=2)

btnplus=Button(top,text="+",bd=5,padx=20,command=lambda:click("+"))
btnplus.grid(row=1,column=4)

btnminus=Button(top,text="-",bd=5,padx=20,command=lambda:click("-"))
btnminus.grid(row=2,column=4)

btnmulti=Button(top,text="x",bd=5,padx=20,command=lambda:click("*"))
btnmulti.grid(row=3,column=4)

btndivide=Button(top,text="/",bd=5,padx=20,command=lambda:click("/"))
btndivide.grid(row=4,column=4)

btnequal=Button(top,text="=",bd=5,padx=20,command=sum)
btnequal.grid(row=5,column=4)

btnquit = Button(top,text="QUIT",bd=5,padx=8,command=quit)
btnquit.grid(row=5,column=1)

btn7=Button(top,text="7",bd=5,padx=15,command=lambda:click(7))
btn7.grid(row=1,column=0)

btn8=Button(top,text="8",bd=5,padx=15,command=lambda:click(8))
btn8.grid(row=1,column=1)

btn9=Button(top,text="9",bd=5,padx=15,command=lambda:click(9))
btn9.grid(row=1,column=2)

btn4=Button(top,text="4",bd=5,padx=15,command=lambda:click(4))
btn4.grid(row=2,column=0)

btn5=Button(top,text="5",bd=5,padx=15,command=lambda:click(5))
btn5.grid(row=2,column=1)

btn6=Button(top,text="6",bd=5,padx=15,command=lambda:click(6))
btn6.grid(row=2,column=2)

top.mainloop()
