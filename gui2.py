from tkinter import *
from PIL import ImageTk, Image
import string
import random

######## WindowConfig #########

setting = Tk()
setting.geometry("500x500")
setting.resizable(width=False, height=False)# blocked enlarge
setting.title('Genpass')
setting.iconbitmap('asset/ico/logo.ico')
setting.config(background='#21282C')# default background

######## Import Image #########

applybtn = Image.open("asset/applybtn.png")
cancelbtn = Image.open("asset/cancelbtn.png")

######## Resize Image #########

#apply
resized_applybtn = applybtn.resize((130, 65), Image.ANTIALIAS)
new_applybtn = ImageTk.PhotoImage(resized_applybtn)

#cancel
resized_cancelbtn = cancelbtn.resize((130, 65), Image.ANTIALIAS)
new_cancelbtn = ImageTk.PhotoImage(resized_cancelbtn)

######## Function #########

def cancel_event():
	setting.destroy
	

######## Frame #########

frame = Frame(setting)
frame.pack(side=BOTTOM)

frame = Frame(root)
frame.pack(side=BOTTOM)

######## Button #########

cancel = Button(frame, image=new_cancelbtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=lambda: copy_paste())
cancel.pack(side=RIGHT)
apply_ = Button(frame, image=new_applybtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=lambda: copy_paste())
apply_.pack(side=LEFT)

######## Print #########
setting.mainloop()