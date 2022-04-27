#import password.py
from tkinter import *
from PIL import ImageTk, Image

#window config
root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)# blocked enlarge
root.title('generate_password')
root.iconbitmap('asset/logo.ico')
root.config(background='#21282C')# default background

#navbarre
menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

root.config(menu=menu)

#exit
root.mainloop()

