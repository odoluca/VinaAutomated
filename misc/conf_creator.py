folder=r"D:\Users\doluc\Downloads\RCSB-PDB-BatchDownload-1587203623"
import os
os.chdir(folder)

flist=os.listdir()
for f in flist:
    cf=open(f[:-4]+".txt","w")
    cf.write() #THE CONTENT GOES HERE
    cf.close()