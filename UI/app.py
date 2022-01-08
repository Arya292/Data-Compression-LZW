import tkinter as tk
from tk import *
from PIL import Image, ImageTk

def show(fr):
    fr.tkraise()

root=tk.Tk()
root.geometry("600x800")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
f1=tk.Frame(root,bg='light blue')
f2=tk.Frame(root,bg="pink")
for frs in(f1,f2):
    frs.grid(row=0,column=0,sticky="nsew")
root.title("COMPRESS ME")

# in first frame 
l0=tk.Label(f1,text="WELCOME",font=24)
l0.pack(pady=20)
img = ImageTk.PhotoImage(Image.open("im1.png"))  
l1=tk.Label(f1,image=img)
l1.pack(pady=80)
mb1=tk.Menubutton(f1,text="Select the file type",fg="blue",)
mb1.menu=tk.Menu(mb1)
mb1["menu"]=mb1.menu
mb1.menu.add_command(label="           Text       ")
mb1.menu.add_command(label="           Image      ")
mb1.pack(side=tk.TOP, pady=0)
go=tk.Button(f1,text="go",command=lambda:show(f2))
go.pack(pady=20)

#in the second frame 
back=tk.Button(f2,text="back",command=lambda:show(f1))
back.pack(pady=20)
 
show(f1)
root.mainloop()
