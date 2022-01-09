import os
import sys
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
        if self.ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"]:
            self.dict+=[chr(425),chr(925)]
            self.text=self.text[:-len(self.ext)-1]
            self.text=self.decompress()
            self.msg=self.strtoimg(self.text,out)
        else:
            self.text = self.text[:-len(self.ext)-1]
            de=self.decompress()
            with open(out,"w") as f:
                f.write(de)
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
        for line in text.split(chr(925)):
            temp=line.split(chr(425))
            for i in range(0,len(temp)):
                temp[i] = [ord(temp[i][j]) for j in range(0, len(temp[i]))]
            pix.append(temp[:-1])
        x,y=len(pix),len(pix[0])
        new=Image.new("RGB",(x,y))
        for i in range(0,x):
            for j in range(0,len(pix[i])):
                new.putpixel((i,j),tuple(pix[i][j]))
        new.save(outfile)
        return "File decompressed successfully"
        

if __name__=="__main__":
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            decompress(i)
