

# Follow for more : @divstech

import wikipedia 
from tkinter import *
from tkinter.messagebox import showinfo

wiki = Tk()
wiki.title("Wikipedia")
wiki.geometry('250x70')
wiki.iconbitmap('wiki.ico')

#Fucntion for searching
def search_wiki():
	search = entry.get()
	answer = wikipedia.summary(search)
	showinfo("Wikipedia Answer",answer)

label = Label(wiki,text="Wikipedia Search :")
label.grid(row=0,column=1)

entry = Entry(wiki)
entry.grid(row=1,column=1)

button = Button(wiki,text="Search",command=search_wiki)
button.grid(row=1,column=2,padx=10)

wiki.mainloop()


