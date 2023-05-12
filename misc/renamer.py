folder=r"D:\Users\doluc\Downloads\RCSB-PDB-BatchDownload-1587203623"
import os
os.chdir(folder)

flist = os.listdir()

for f in flist:
    if f.endswith("2") or f.endswith("1"):
        print(f)
        try:
            os.rename(f,f[:-1])
        except:
            os.rename(f,f[:4]+"_2"+f[-5:-1])
