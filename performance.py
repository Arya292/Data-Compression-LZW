from decompress import decompress
from compress import compress
import time
import os

for i in range(1,4):
    t=time.time()
    compress(f"./data/file{i}.txt")
    comp_time = (time.time()-t)
    size1,size2=os.path.getsize(f"./data/file{i}.txt"),os.path.getsize(f"./data/file{i}.lzw")
    t=time.time()
    decompress(f"./data/file{i}.lzw", f"./data/file{i}_d.txt")
    decomp_time = (time.time()-t)
    size3=os.path.getsize(f"./data/file{i}_d.txt")
    print("Size before compression:", size1/1024, "KB")
    print("Size after compression:", size2/1024, "KB")
    print("Size after decompression:",size3/1024,"KB")
    print("Compression ratio:",size2/size1)
    print(f"Compress time: {comp_time}s")
    print(f"Decompress time: {decomp_time}s")
    print("="*50)