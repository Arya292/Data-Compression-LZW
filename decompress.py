import os
import sys
import numpy as np
from PIL import Image

class decompress():
    def __init__(self,file,out=None):
        self.dict = [chr(a) for a in range(256)]
        try : self.text=open(file,"r").read()
        except :
            self.msg="File is not decompressable"
            return
        self.ext=self.text.split()[-1]
        if not out:
            out = os.path.splitext(file)[0]+self.ext
        else:
            out=os.path.dirname(file)+"/"+out
        if self.ext in [".png", ".jpg", ".jpeg", ".tif", ".bmp", ".gif",".tiff"]:
            self.dict+=[chr(256),chr(425)]
            self.text=self.text[:-len(self.ext)-1]
            self.text=self.decompress()
            self.msg=self.strtoimg(self.text,out)
        else:
            self.text = self.text[:-len(self.ext)-1]
            de=self.decompress()
            with open(out,"w") as f:
                f.write(de)
            print("File saved to "+out)
            self.msg= "File decompressed successfully"


    def decompress(self):
        c = ""
        self.text = list(map(int, self.text.strip().split(",")))
        prev = self.text[0]
        self.len = len(self.text)
        out = self.dict[prev]
        i = 1
        while i < self.len:
            print(i/self.len,end="\r")
            if self.text[i] >= len(self.dict):
                s = self.dict[prev]
                s = s+c
            else:
                s = self.dict[self.text[i]]
            out += s
            c = s[0]
            self.dict.append(self.dict[prev]+c)
            prev = self.text[i]
            i += 1
        return out
    
    def strtoimg(self,text,outfile):
        pix=[]
        pix=text.split(chr(425))
        r,g,b=list(map(list,np.array_split(pix,3)))
        for i in range(len(r)):
            r[i]=[ord(j)-1 for j in r[i]]
            g[i]=[ord(j)-1 for j in g[i]]
            b[i]=[ord(j)-1 for j in b[i]]
        x,y=len(r),len(r[0])
        new=Image.new("RGB",(x,y))
        for i in range(0,x):
            for j in range(0,y):
                new.putpixel((i,j),(r[i][j],g[i][j],b[i][j]))
        new.save(outfile)
        print("Image Saved to "+outfile)
        return "File decompressed successfully"
        

if __name__=="__main__":
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            decompress(i)
