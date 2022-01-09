import os
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import Image, ImageTk
from compress import compress
from decompress import decompress


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("./assets/bg.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
        self.background.image=self.background_image

filename=""
color1, color2, color3 = ["#f9b8b1", "#f84791", "#25388e"]

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
        l2.configure(image=preview,height=x,width=y,bg=color1)
        l2.image = preview
    else:
        try:
            text=open(filename,"r").read()
            l2.configure(text=text,bg=color1,anchor=W)
            l2.image=None
            new=scrolledtext(l2,width=50,height=10,bg=color1)
        except:
            l2.configure(text="Unknown File format")
            l2.text="Unknown File format"

    


root=Tk()
root.geometry("800x450")
root.iconphoto(True, PhotoImage(file="assets/icon.png"))
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
f1=Example(root)
f2=Frame(root,bg=color1)

for frs in (f1,f2):
    frs.grid(row=0,column=0,sticky="nsew")
root.title("COMPRESS ME")

# in first frame 
# img=Image.open("static/bg.png")
# img=img.resize((800,450))
# bg=ImageTk.PhotoImage(img)
# canv=Canvas(f1)
# canv.pack(fill="both",expand=True)
# canv.create_image(0, 0, image=bg, anchor="nw")

l0=Label(f1,text="WELCOME",font=1000,fg="green")
l0.place(relx=0.5,rely=0.1,anchor="center",relheight=0.1,relwidth=0.3)

go = Button(f1, text="go", command=lambda: show(f2), border=0,bg=color2, fg=color3, activebackground=color3, activeforeground=color2)
go.place(relx=0.5, rely=0.99, anchor="s")

#in the second frame
back = Button(f2, text="back", command=lambda: show(f1),border=0, bg=color2, fg=color3,activebackground=color3,activeforeground=color2)
back.place(relx=0.5, rely=0.99, anchor="s")

temp=Label(f2,text="File Compressor",font=1000,fg="green",bg=color1)
temp.place(relx=0.5, rely=0.03, relheight=0.1, relwidth=0.5, anchor="n")

Compress=Button(f2,text="COMPRESS",bg=color2,command=lambda:compress(filename),border=0,fg=color3,activebackground=color3,activeforeground=color2)
Decompress= Button(f2,text="DECOMPRESS",bg=color2,fg=color3,command=lambda:decompress(filename),border=0,activebackground=color3,activeforeground=color2)
Compress.place(relx=0.5, rely=0.84,relheight=0.08, relwidth=0.25)
Decompress.place(relx=0.75, rely=0.84, relheight=0.08, relwidth=0.25)

l2=Label(f2)
l2.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

file_disp = Label(f2, text="No File selected", width=100, height=1, fg=color3, bg=color2)
file_button = Button(f2, text="Browse Files", command=browse ,border=0,fg=color3,bg=color2,activebackground=color3,activeforeground=color2)
file_disp.place(relx=0, rely=0.13, height=25, relwidth=0.75)
file_button.place(relx=0.75, rely=0.13, height=25,relwidth=0.25)

show(f1)
root.mainloop()