#import password.py
from tkinter import *
from PIL import ImageTk, Image
import string
import random

######## WindowConfig #########

root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)# blocked enlarge
root.title('Genpass')
root.iconbitmap('asset/logo.ico')
root.config(background='#21282C')# default background

######## NavBar #########

menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

root.config(menu=menu)

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
password = Label(root, text="- - - -", font=("Pixeled", 9), fg="#003F3F", bg="#808080")
password.place(x=225, y=195)

#Bar Image
barre = Label(root, image=new_barre, borderwidth=0, bg="#21282C")
barre.place(x=25, y=80)

######## Boutton #########

#RegenBtn
regen = Button(root, image=new_regenbtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=password)
regen.place(x=200, y=250)

#CopyBtn
copy = Button(root, image=new_copybtn, borderwidth=0, bg="#21282C", activebackground="#21282C")
copy.place(x=380, y=190)

#Setting
setting = Button(root, image=new_settingbtn, borderwidth=0, bg="#21282C", activebackground="#21282C")
setting.place(x=400, y=380)

def password():
	lettres = string.ascii_letters
	chiffres = string.digits
	ponc = string.punctuation

	l = 10 #lenght (default)

	char = ""
	char += lettres + chiffres + ponc

	passe = "".join(random.choices(char, k=l))
	print(passe)
	password.config(text=f"{passe}")

######## Print #########
root.mainloop()

