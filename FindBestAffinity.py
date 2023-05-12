import os

dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\DHODH_DrugBank_ligands\dockings"
txt_files=[x for x in os.listdir(dir) if x.endswith(".txt")]
# print("\n".join(txt_files))
pretext="   1       "

min_txt=[]
min_scores=[]
min_score=-12.5


counter=0
for txt_file in txt_files:
    with open(dir+"\\"+txt_file,"r") as f:
        for line in f.readlines():
            if line.startswith(pretext):
                score=float(line.split()[1])
                if score<min_score:
                    counter+=1
                    min_scores.append(score)
                    min_txt.append(txt_file)
for a in zip(min_txt,min_scores):
    print(a[0],a[1])
print(counter,len(txt_files))

