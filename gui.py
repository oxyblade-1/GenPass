from tkinter import *
from PIL import ImageTk, Image
import pyperclip
import os
import string
import random

os.system("cls")

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
pass_label = Label(root, text="PASSWORD", font=("Poppins", 15), fg="#00BCBC", bg="#21282C")
pass_label.place(x=190, y=150)

#number Max Bar
copy_label = Label(root, text="20 words", font=("Poppins", 12), fg="#404040", bg="#21282C")
copy_label.place(x=35, y=55)

#message "regenerate"
regen_label = Label(root, text="regenerate", font=("Poppins", 10), fg="#404040", bg="#21282C")
regen_label.place(x=220, y=315)

#Input Image (au dessus de password message)
input_l = Label(root, image=new_inputlabel, borderwidth=0, bg="#21282C")
input_l.place(x=150, y=190)

#password message
password_message = Label(root, text=" ", font=("Poppins", 12), fg="#003F3F", bg="#808080")
password_message.place(x=215, y=200)

#Bar Image
barre = Label(root, image=new_barre, borderwidth=0, bg="#21282C")
barre.place(x=25, y=80)

######## Function #########

def copy_paste(text):
	pyperclip.copy(text)


def password():
	global passe
	lettres = string.ascii_letters
	chiffres = string.digits
	ponc = string.punctuation

	l = 10 or pass_lenght #lenght (default)

	char = ""
	char += lettres + chiffres + ponc

	passe = "".join(random.choices(char, k=l))
	password_message.config(text=f"{passe}")


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

	#True
	on_onbtn = Image.open("asset/button/Tbtn_on.png")
	on_offbtn = Image.open("asset/button/Tbtn_off.png")

	#False
	off_offbtn = Image.open("asset/button/Fbtn_off.png")
	off_onbtn = Image.open("asset/button/Fbtn_on.png")
	#bg = PhotoImage(file="asset/setting_font.png")

	######## Resize Image #########

	#apply
	resized_applybtn = applybtn.resize((120, 60), Image.ANTIALIAS)
	new_applybtn = ImageTk.PhotoImage(resized_applybtn)

	#cancel
	resized_cancelbtn = cancelbtn.resize((120, 60), Image.ANTIALIAS)
	new_cancelbtn = ImageTk.PhotoImage(resized_cancelbtn)

	#True
	resized_on_onbtn = on_onbtn.resize((30, 30), Image.ANTIALIAS)
	new_on_onbtn = ImageTk.PhotoImage(resized_on_onbtn)

	resized_on_offbtn = on_offbtn.resize((30, 30), Image.ANTIALIAS)
	new_on_offbtn = ImageTk.PhotoImage(resized_on_offbtn)


	# #False
	# resized_applybtn = applybtn.resize((120, 60), Image.ANTIALIAS)
	# new_applybtn = ImageTk.PhotoImage(resized_applybtn)
	# resized_applybtn = applybtn.resize((120, 60), Image.ANTIALIAS)
	# new_applybtn = ImageTk.PhotoImage(resized_applybtn)

	######## Frame #########

	frame = Frame(setting)
	frame.pack(side=BOTTOM)

	######## Entry #########

	lenght = Entry(setting, font=("Poppins", 10), fg="#003F3F", bg="#808080", width=8)
	lenght.place(x=350, y=150)

	######## Function #########

	def btn_changer1():
		#Button_letter
		on_label = Radiobutton(setting, image=new_on_onbtn, borderwidth=0, value=1, indicatoron=0, activebackground="#21282C", bg="#21282C", command=btn_changer1)
		on_label.place(x=190, y=100)

		#Button_number
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=2, indicatoron=0, activebackground="#21282C", bg="#21282C")
		on_label.place(x=190, y=170)

		#Button_punctuation
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=3, indicatoron=0, activebackground="#21282C", bg="#21282C")
		on_label.place(x=190, y=270)

	def btn_changer2():
		#Button_letter
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=1, indicatoron=0, activebackground="#21282C", bg="#21282C", command=btn_changer1)
		on_label.place(x=190, y=100)

		#Button_number
		on_label = Radiobutton(setting, image=new_on_onbtn, borderwidth=0, value=2, indicatoron=0, activebackground="#21282C", bg="#21282C")
		on_label.place(x=190, y=170)

		#Button_punctuation
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=3, indicatoron=0, activebackground="#21282C", bg="#21282C")
		on_label.place(x=190, y=270)

	def btn_changer3():

		#Button_letter
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=1, indicatoron=0, activebackground="#0A2E00", bg="#21282C", command=btn_changer1)
		on_label.place(x=190, y=100)

		#Button_number
		on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=2, indicatoron=0, activebackground="#0A2E00", bg="#21282C")
		on_label.place(x=190, y=170)

		#Button_punctuation
		on_label = Radiobutton(setting, image=new_on_onbtn, borderwidth=0, value=3, indicatoron=0, activebackground="#0A2E00", bg="#21282C")
		on_label.place(x=190, y=270)

	def lenght_get():
		global pass_lenght
		pass_lenght = lenght.get()
		print("\033[32msave lenght")


	######## Label #########

	#fontground = Label(setting, image=bg)
	#fontground.place(x=0, y=0, relwidth=1, relheight=1)
	#relwidth/ relheight combler les bordures !

	lenght_label = Label(setting, text="lenght", font=("Poppins", 10), fg="#404040", bg="#21282C")
	lenght_label.place(x=360, y=120)

	#letter
	letter_label = Label(setting, text="LETTER", font=("Poppins", 12), fg="#004C4C", bg="#007F7F")
	letter_label.place(x=70, y=100)

	#number
	number_label = Label(setting, text="NUMBER", font=("Poppins", 12), fg="#004C4C", bg="#007F7F")
	number_label.place(x=70, y=180)

	#punctuation
	punctuation_label = Label(setting, text="PUNCTUATION", font=("Poppins", 12), fg="#004C4C", bg="#007F7F")
	punctuation_label.place(x=50, y=270)

	######## Button #########
	a = IntVar()
	b = IntVar()

	#Button_letter
	on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=1, indicatoron=0, activebackground="#0A2E00", bg="#21282C", command=btn_changer1)
	on_label.place(x=190, y=100)

	#Button_number
	on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=2, indicatoron=0, activebackground="#0A2E00", bg="#21282C", command=btn_changer2)
	on_label.place(x=190, y=170)

	#Button_punctuation
	on_label = Radiobutton(setting, image=new_on_offbtn, borderwidth=0, value=3, indicatoron=0, activebackground="#0A2E00", bg="#21282C", command=btn_changer3)
	on_label.place(x=190, y=270)

	cancel = Button(frame, image=new_cancelbtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=setting.destroy)
	cancel.pack(side=LEFT)
	apply_ = Button(frame, image=new_applybtn, borderwidth=0, bg="#21282C", activebackground="#21282C", command=lenght_get)
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