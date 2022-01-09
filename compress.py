import os
from PIL import Image 

def compress(file):
    name,extension=os.path.splitext(file)
    if extension==".txt":
        text_compress(file)
    elif extension in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
        image_compress(file)
    else :
        print("unknown file format")
    
def text_compress(text):
    with open(text) as f:
        contents = f.read()
    compress_any(contents)
    

def image_compress(image):
    im=Image.open(image)
    x,y=im.size[0],im.size[1]
    s=""
    for i in range(0,x):
        for j in range(0,y):
            temp=im.getpixel((i,j))
            a,b,c=temp[0],temp[1],temp[2]
            s=s+str(a)+","+str(b)+","+str(c)+" "
    s=s+"\n"
    compress_any(s)
def compress_any(contents):
    table= [chr(i) for i in range(256)]
    table.append(chr(425))
    table.append(chr(945))
    output,a="",contents[0]
    i=1
    while i<=(len(contents)-1):
        b=contents[i]
        if a+b in table:
            a=a+b
        else:
            output=output+ str(table.index(a))+","
            table.append(a+b)
            a=b
        i=i+1
    output=output+ str(table.index(a))+" "
    new=open("compressed.txt","w+")
    new.write(output)
    
