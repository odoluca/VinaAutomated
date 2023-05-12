import matplotlib.pyplot as plt
from numpy import arange
import summarize_results

q=summarize_results.read_summary()
z={}
for k,vs in q.items():
    for vk,vv in vs.items():
        try:
             z[vk][k]=float(vv)
        except:
            try:
                z[vk]={k:float(vv)}
            except:
                pass

a2=plt.hist(z["6lzl"].values(),bins=arange(-15,0,0.1),color="black")
a1=plt.hist(z["6j3c"].values(),bins=arange(-15,0,0.1),alpha=0.5,color="gray")
plt.xlabel("affinity (kcal/mol)")
plt.ylabel("drug count")
