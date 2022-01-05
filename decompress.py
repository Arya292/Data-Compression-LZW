import os
import sys

class decompress():
    def __init__(self,file,out=None):
        if not out:
            out = os.path.splittext(file)[0]+".txt"
        self.dict=[chr(a) for a in range(256)]
        self.file=file
        de=self.decompress(file)
        with open(out,"w") as f:
            f.write(de)


    def decompress(text):
        c = ""
        text = list(map(int, text.strip().split(",")))
        prev = text[0]
        out = self.dict[prev]
        i = 1
        while i < len(text):
            if text[i] >= len(dct):
                s = self.dict[prev]
                s = s+c
            else:
                s = self.dict[text[i]]
            out += s
            c = s[0]
            dict.append(self.dict[prev]+c)
            prev = text[i]
            i += 1
        return out

if __name__=="__main__":
    for i in sys.argv[1:]:
        if os.path.isfile(i):
            decompress(i)
