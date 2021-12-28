def decompress(file):
    text = open(file).read()
    c=""
    dct = [chr(a) for a in range(256)]
    text=list(map(int,text.strip().split()))
    prev=text[0]
    out=dct[prev]
    i=1
    while i<len(text):
        if text[i] >= len(dct):
            s=dct[prev]
            s=s+c
        else:
            s=dct[text[i]]
        out+=s
        c=s[0]
        dct.append(dct[prev]+c)
        prev=text[i]
        i+=1
    file=file[:file.rfind(".")]
    file=file.replace("_compressed","")
    with open(f"{file}_decompressed.txt","wb") as f:
        f.write(out.encode())
    return f"{file}_decompressed.txt"

# file=input()
compress(input())
decompress("output.txt")
