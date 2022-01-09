import os
import sys

class decompress():
    def __init__(self,file,out=None):
        self.text=open(file,"r").read()
        self.ext=self.text.split()[-1]
        if not out:
            out = os.path.splitext(file)[0]+self.ext
        if self.ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"]:
            self.dict=[str(i) for i in range(10)]+[" ",",","\n"]
            self.text=self.text[:-len(self.ext)-1]
            self.text=self.decompress()
            slef.msg=self.strtoimg(self.text,out)
        else:
            self.dict = [chr(a) for a in range(256)]
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
    
    def strtoimg(text,outfile):
        pix=[]
        for line in text.split("\n"):
            temp=line.split()
            for i in range(0,len(temp)):
                temp[i]=list(map(int,temp[i].split(",")))
            pix.append(temp)
        x,y=len(pix),len(pix[0])
        new=Image.new("RGB",(x,y))
        for i in range(0,x):
            for j in range(0,y):
                new.putpixel((i,j),(pix[i][j][0],pix[i][j][1],pix[i][j][2]))
        return new
        new.save(outfile)
        return "File decompressed successfully"
        

if __name__=="__main__":
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            decompress(i)
