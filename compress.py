def compress(text):
    ascii_list= [chr(i) for i in range(128)]
    output,a="",text[0]
    i=1
    while i<=(len(text)-1):
        b=text[i]
        if a+b in ascii_list:
            a=a+b
        else:
            output=output+ str(ascii_list.index(a))+" "
            ascii_list.append(a+b)
            a=b
        i=i+1
    output=output+ str(ascii_list.index(a))+" "
    return output

file=input()
print(compression(file))
