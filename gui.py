#import password.py
from tkinter import *
from PIL import ImageTk, Image

#window config
root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)# blocked enlarge
root.title('Genpass')
root.iconbitmap('asset/logo.ico')
root.config(background='#21282C')# default background

#navbarre
menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

root.config(menu=menu)

#Label
pass_label = Label(root, text="password", font=("Pixeled", 15), fg="#00BCBC", bg="#21282C")
pass_label.pack(expand=YES)
regenerate = Label(root, text="20", font=("Pixeled", 12), fg="#404040", bg="#21282C")
regenerate.pack(side=LEFT)
regenerate = Label(root, text="regenerate", font=("Pixeled", 10), fg="#1E2122", bg="#21282C")
regenerate.pack(expand=YES)

#Picture
img_regen = PhotoImage(file="asset/regenbtn.png")

#BTN
regen = Button(root, image=img_regen, borderwidth=0, bg="#21282C")
regen.pack()

#print
root.mainloop()

