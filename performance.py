from decompress import decompress
from compress import compress
import time
import os

t=time.time()
compress("./data/file2.txt")
print(f"Compress time: {time.time()-t}")
print("Size before compression:",os.path.getsize("./data/file2.txt"))
print("Size after compression:",os.path.getsize("./data/file2.lzw"))

t=time.time()
decompress("./data/file2.lzw", "./data/file2_d.txt")
print(f"Decompress time: {time.time()-t}")
print("Size before decompression:",os.path.getsize("./data/file2.lzw"))
print("Size after decompression:",os.path.getsize("./data/file2_d.txt"))