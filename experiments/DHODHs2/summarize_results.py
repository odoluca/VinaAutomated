import os

def write_summary(dir=os.curdir):
    os.chdir(dir)
    completed_docking_files=[x for x in os.listdir("dockings") if x.endswith("txt")]
    pretext="   1       "
    # completed_dockings=[ [x[:-4].split("_")] for x in completed_dockings]

    receptors=[x[:-6] for x in os.listdir("receptors") if x.endswith("pdbqt")]

    summary={}
    for r in receptors:
        summary.update({r:{}})

    ligand_set=set()
    for cd in completed_docking_files:

        with open("dockings\\"+cd) as f:
            for line in f.readlines():
                if line.startswith(pretext):
                    best_score=line.split()[1]
        r,l=tuple(cd[:-4].split("_"))
        ligand_set.add(l)
        summary[r].update({l:best_score})


    with open("summary.csv","w") as sf:
        sf.write("sep=,\n,")
        for l in ligand_set:
            sf.write(l)
            sf.write(",")
        sf.write("\n")
        for r in summary.keys():
            sf.write(r)
            sf.write(",")
            for l in ligand_set:
                try:
                    sf.write(summary[r][l])
                except:
                    pass
                sf.write(",")
            sf.write("\n")

def read_summary(dir=os.curdir):
    os.chdir(dir)
    with open("summary.csv", "r") as sf:
        sf.readline()
        ligands=sf.readline().split(",")
        data={}
        for l in ligands:
            data.update({l:{}})
        receptors=[]
        errors=[]
        for line in sf.readlines():
            line=line.strip("\n,").split(",")
            receptors.append(line[0])
            for i in range(len(line)):
                # try:
                data[ligands[i]].update({line[0]:line[i]})
                # except:
                #     errors.append(ligands[i])
    return data


