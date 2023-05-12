file=open("drug interactions","r")

interactions={}
active_key=""
for line in file.readlines():
    if line.lower().startswith("dock"):
        active_key =line.split("\t")[1].strip()
        interactions[active_key]=[]
    else:

        objs=line.split()
        for obj in objs:
            if obj.find("UNL1")==-1 and obj.find("A:")>-1:
                obj=obj.split(":")
                interactions[active_key].append( obj[1] )
                break

aminoacids={}
for k,vs in interactions.items():
    for v in set(vs):
        if  v not in aminoacids :
            aminoacids[v]=[k]
        else:
            aminoacids[v].append(k)

aas=list( aminoacids.keys())

drugs=set()
for v in aminoacids.values():
    for i in v:
        drugs.add(i)
drugs=list(drugs)
drugs.sort()
print("\t".join(aas))
for i in drugs:
    print()
    print(i, end="\t")
    for j in aas:
        if i in aminoacids[j]:
            print("X", end="\t")
        else:
            print("", end="\t")

