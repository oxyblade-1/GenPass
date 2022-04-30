from tkinter import *
from PIL import ImageTk, Image
import pyperclip
import string
import random

######## WindowConfig #########

root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)# blocked enlarge
root.title('Genpass')
root.iconbitmap('asset/ico/logo.ico')
root.config(background='#21282C')# default background

######## Import Image #########

regenbtn = Image.open("asset/regenbtn.png")#boutton regenerate
copybtn = Image.open("asset/copybtn.png")#boutton copy
barre_empty = Image.open("asset/barre_empty.png")#image barre
settingbtn = Image.open("asset/setting.png")#image barre
inputlabel = Image.open("asset/input.png")#image barre

######## Resize Image #########

#RegenBtn
resized_regenbtn = regenbtn.resize((120, 60), Image.ANTIALIAS)
new_regenbtn = ImageTk.PhotoImage(resized_regenbtn)

#CopyBtn
resized_copybtn = copybtn.resize((40, 40), Image.ANTIALIAS)
new_copybtn = ImageTk.PhotoImage(resized_copybtn)

#Barre
resized_barre = barre_empty.resize((100, 300), Image.ANTIALIAS)
new_barre = ImageTk.PhotoImage(resized_barre)

#Setting
resized_setting = settingbtn.resize((80, 80), Image.ANTIALIAS)
new_settingbtn = ImageTk.PhotoImage(resized_setting)

#Input
resized_input = inputlabel.resize((200, 50), Image.ANTIALIAS)
new_inputlabel = ImageTk.PhotoImage(resized_input)

######## Label #########

#main message "password"
pass_label = Label(root, text="password", font=("Pixeled", 15), fg="#00BCBC", bg="#21282C")
pass_label.place(x=170, y=100)

#number Max Bar
copy_label = Label(root, text="20 words", font=("Pixeled", 12), fg="#404040", bg="#21282C")
copy_label.place(x=30, y=30)

#message "regenerate"
regen_label = Label(root, text="regenerate", font=("Pixeled", 10), fg="#1E2122", bg="#21282C")
regen_label.place(x=200, y=300)

#Input Image (au dessus de password message)
input_l = Label(root, image=new_inputlabel, borderwidth=0, bg="#21282C")
input_l.place(x=150, y=190)

#password message
password_message = Label(root, text=" ", font=("Pixeled", 9), fg="#003F3F", bg="#808080")
password_message.place(x=200, y=195)

#Bar Image
barre = Label(root, image=new_barre, borderwidth=0, bg="#21282C")
barre.place(x=25, y=80)

######## Function #########

def password():
	global passe
	lettres = string.ascii_letters
	chiffres = string.digits
	ponc = string.punctuation

	l = 10 #lenght (default)

	char = ""
	char += lettres + chiffres + ponc

	passe = "".join(random.choices(char, k=l))
	password_message.config(text=f"{passe}")

def copy_paste(text):
	copy = pyperclip.copy(text)

def setting_window():

	######## Setting window Config #########

	setting = Toplevel()
	setting.geometry("450x450")
	setting.resizable(width=False, height=False)# blocked enlarge
	setting.title('Setting')
	setting.iconbitmap('asset/ico/logo.ico')
	setting.config(background='#21282C')# default background

	######## Import Image #########

	applybtn = Image.open("asset/applybtn.png")
	cancelbtn = Image.open("asset/cancelbtn.png")
	#bg = PhotoImage(file="asset/setting_font.png")

	######## Resize Image #########

	#apply
	resized_applybtn = applybtn.resize((120, 60), Image.ANTIALIAS)
	new_applybtn = ImageTk.PhotoImage(resized_applybtn)

	#cancel
	resized_cancelbtn = cancelbtn.resize((120, 60), Image.ANTIALIAS)
	new_cancelbtn = ImageTk.PhotoImage(resized_cancelbtn)

	######## Frame #########

	frame = Frame(setting)
	frame.pack(side=BOTTOM)

	######## Entry #########

	lenght = Entry(setting, font=("Pixeled", 7), fg="#003F3F", bg="#808080", width=8)
	lenght.place(x=100, y=200)

	######## Label #########

	#fontground = Label(setting, image=bg)
	#fontground.place(x=0, y=0, relwidth=1, relheight=1)
	#relwidth/ relheight combler les bordures !

	#Lenght

	#

	######## Button #########

	cancel = Button(frame, image=new_cancelbtn, borderwidth=0, bg="#21282C", activebackground="#21282C")
	cancel.pack(side=LEFT)
	apply_ = Button(frame, image=new_applybtn, borderwidth=0, bg="#21282C", activebackground="#21282C")
	apply_.pack(side=RIGHT)


	######## Print setting #########
	setting.mainloop()


######## Boutton #########

#CopyBtn
copy = Button(root, image=new_copybtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=lambda: copy_paste(passe))
copy.place(x=380, y=190)

#Setting
setting_ = Button(root, image=new_settingbtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=setting_window)
setting_.place(x=400, y=380)

#RegenBtn
regen = Button(root, image=new_regenbtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=password)
regen.place(x=200, y=250)


######## Print root #########
root.mainloop()