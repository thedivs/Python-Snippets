

#Author : DIVS TECH

import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk

win = Tk()
win.title("QR Code Generator")
win.config(background='#fed304')

def generate():
	text = entry1.get()
	qr = pyqrcode.create(text)
	file_name = "my qrcode"
	save_path = r"C:\Users\FSociety\Desktop\ "
	name = save_path+file_name+'.png'
	qr.png(name,scale=10)
	image = Image.open(name)
	image = image.resize((400,400), Image.ANTIALIAS)
	image = ImageTk.PhotoImage(image)
	win.imagelabel.config(image=image)
	win.imagelabel.photo = image
#pip install pypng
text = ttk.Label(win,text="Enter text or link :")
text.grid(row=0,column=0,padx=3,pady=3)

entry1 = ttk.Entry(win,width=10)
entry1.grid(row=0,column=1,padx=3,pady=3)

button = ttk.Button(win,text="Generate",command=generate)
button.grid(row=0,column=2,padx=3,pady=3)

show_qr = ttk.Label(win,text="QR CODE:")
show_qr.grid(row=1,column=0,padx=3,pady=3)

win.imagelabel = ttk.Label(win,background='#fed304')
win.imagelabel.grid(row=2,column=0,padx=3,pady=3,columnspan=3)

win.mainloop()