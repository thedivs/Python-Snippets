

# Author : Divstech

import socket
from tkinter import * 
import pyperclip

top = Tk()
top.geometry("400x200")
top.title("IP Generator App")
#Adding Window Icon 
top.iconbitmap('ip_address.ico')
ipgen = StringVar()

# Function for generating ip address
def ipgenerate():
	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	ipgen.set(ip_address)

#Function for coping ip address
def copyip():
	ip_add = ipgen.get()
	pyperclip.copy(ip_add)

Label(top, text = "IP Generator App",font="calibri 20 bold").pack()
			
Button(top,text="Generate Your IP",command=ipgenerate).pack(pady=7)
Entry(top,textvariable=ipgen).pack(pady=3)
Button(top,text="Copy IP Address",command=copyip).pack()

top.mainloop()