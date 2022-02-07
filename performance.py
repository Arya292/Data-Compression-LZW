from decompress import decompress
from compress import compress
import time
import os

def check(inf,outf):
    t=time.time()
    compress(inf)
    comp_time = (time.time()-t)
    size1,size2=os.path.getsize(inf),os.path.getsize(outf)
    t=time.time()
    decompress(outf, "_d".join(os.path.splitext(inf))[5:])
    decomp_time = (time.time()-t)
    size3=os.path.getsize("_d".join(os.path.splitext(inf)))
    print("Size before compression:", size1/1024, "KB")
    print("Size after compression:", size2/1024, "KB")
    print("Size after decompression:",size1/1024,"KB")
    print("Compression ratio:",size2/size1)
    print(f"Compress time: {comp_time}s")
    print(f"Decompress time: {decomp_time}s")
    print("="*50)

check("data/file1.txt","data/file1.lzw")
check("data/file2.txt","data/file2.lzw")
check("data/file3.txt","data/file3.lzw")

check("data/check.tif","data/check.lzw")
check("data/cup.tif","data/cup.lzw")
check("data/small.tif","data/small.lzw")
