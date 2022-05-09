from tkinter import *

root = Tk()

button = Radiobutton(root, text="button", variable=IntVar(), value=1, indicatoron=0)
button.pack(expand=YES)

root.mainloop()