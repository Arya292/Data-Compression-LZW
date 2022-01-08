import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from compress import compress
from decompress import decompress

filename=""
color1="pink"
color2="light blue"

def isimg(filename):
    name,ext=os.path.splitext(filename)
    if ext in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
        return True
    return False

def show(fr):
    fr.tkraise()


def browse():
    global filename, color1, color2
    filetypes = (("all files", "*.*"),
                 ("Text files", "*.txt*"),
                 ("Image", "*.png*"),
                 ("JPEG", "*.jpg*"),
                 ("gif", "*.gif*"))
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=filetypes)
    file_disp.configure(text="File Opened: "+filename)
    if isimg(filename):
        img = Image.open(filename)
        x, y = img.size
        print(filename,x,y)
        preview = ImageTk.PhotoImage(img)
        l2.configure(image=preview,height=x,width=y)
        l2.image = preview
    else:
        try:
            text=open(filename,"r").read()
            l2.configure(text=text,bg=color1,anchor=W)
            l2.text=text
            l2.anchor=W
        except:
            l2.configure(text="Unknown File format")
            l2.text="Unknown File format"

    


root=Tk()
root.geometry("600x800")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
f1=Frame(root,bg=color2)
f2=Frame(root,bg=color1)

for frs in(f1,f2):
    frs.grid(row=0,column=0,sticky="nsew")
root.title("COMPRESS ME")

# in first frame 
l0=Label(f1,text="WELCOME",font=600,fg="green")
l0.pack(pady=60)
img = ImageTk.PhotoImage(Image.open("data/im1.png"))
l1=Label(f1,image=img)
l1.pack(pady=80)

go=Button(f1,text="go",command=lambda:show(f2))
go.pack(pady=70,expand=FALSE)

#in the second frame 

back = Button(f2, text="back", command=lambda: show(f1))
back.pack(side=BOTTOM, pady=40)


temp=Label(f2,text="File Compressor",font=600,fg="green",bg=color1)
temp.pack(side=TOP,pady=50)

Compress=Button(f2,text="COMPRESS",bg="violet",command=lambda:compress(filename))
Decompress= Button(f2,text="DECOMPRESS",bg="violet",command=lambda:decompress(filename))
Compress.pack(side=BOTTOM, padx=30,)
Decompress.pack(side=BOTTOM,padx=40,pady=10)

l2=Label(f2)
l2.pack()

file_disp = Label(f2, text="File Explorer", width=100, height=4, fg="black", bg=color1)
file_button = Button(f2, text="Browse Files", command=browse)
file_disp.pack(side=TOP)
file_button.pack(side=BOTTOM)

show(f2)
root.mainloop()
