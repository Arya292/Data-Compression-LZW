from decompress import decompress
from compress import compress

opt=int(input("1.compress\n2.decompress\nSelect:"))
file=input("Enter the Filename:")
out = input(f"Enter the output file name(default {os.path.splitdrive(file)[0]}.txt):")
if opt==1:
    compress(file)
elif opt==2:
    decompress(file,out)