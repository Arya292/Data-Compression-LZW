import os
import sys

class decompress():
    def __init__(self,file,out=None):
        if not out:
            out = os.path.splitext(file)[0]+".txt"
        self.dict=[chr(a) for a in range(256)]
        self.text=open(file,"r").read()
        de=self.decompress()
        with open(out,"w") as f:
            f.write(de)


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

if __name__=="__main__":
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            decompress(i)
