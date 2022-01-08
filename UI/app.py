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
l0=tk.Label(f1,text="WELCOME",font=600,fg="green")
l0.pack(pady=60)
img = ImageTk.PhotoImage(Image.open("im1.png"))  
l1=tk.Label(f1,image=img)
l1.pack(pady=80)

go=tk.Button(f1,text="go",command=lambda:show(f2))
go.pack(pady=70)

#in the second frame 
temp=tk.Label(f2,text="")
temp.pack(side=tk.TOP,pady=50)
Compress=tk.Button(f2,text="COMPRESS",bg="violet")
Compress.pack(side=tk.TOP,padx=30,pady=10)
Decompress= tk.Button(f2,text="DECOMPRESS",bg="violet")
Decompress.pack(side=tk.TOP,padx=40)


back=tk.Button(f2,text="back",command=lambda:show(f1))
back.pack(side =tk.BOTTOM,pady=40)

 
show(f1)
root.mainloop()
