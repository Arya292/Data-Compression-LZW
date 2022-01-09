from PIL import Image

image = "c1.png"
im = Image.open(image)
x, y = im.size[0], im.size[1]
s = ""
for i in range(0, x):
    for j in range(0, y):
        temp = im.getpixel((i, j))
        a, b, c = temp[0], temp[1], temp[2]
        s = s+str(a)+","+str(b)+","+str(c)+" "
    s = s+"\n"
    s=compress(s)

new = open("s.txt", "w+")
new.write(s)
new.close()

pix=[]
with open("s.txt") as f:
    for line in f:
        temp=line.split()
        for i in range(0,len(temp)):
            temp[i]=list(map(int,temp[i].split(",")))
        pix.append(temp)
x,y=len(pix),len(pix[0])
new=Image.new("RGB",(x,y))
for i in range(0,x):
    for j in range(0,y):
        new.putpixel((i,j),(pix[i][j][0],pix[i][j][1],pix[i][j][2]))
new.save("c2.png")