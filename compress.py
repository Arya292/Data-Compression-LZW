def compress(txt):
    with open(txt) as f:
        contents = f.read()
    table= [chr(i) for i in range(256)]
    output,a="",contents[0]
    i=1
    while i<=(len(contents)-1):
        b=contents[i]
        if a+b in table:
            a=a+b
        else:
            output=output+ str(table.index(a))+" "
            table.append(a+b)
            a=b
        i=i+1
    output=output+ str(table.index(a))+" "
    new=open("Compressed.txt","w+")
    new.write(output)

file=input()
compress(file)
