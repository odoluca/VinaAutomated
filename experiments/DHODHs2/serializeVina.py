
# We will focus these structures:3W7R,3ZWS,3ZWT,2WV8,4IGH,4OQV,5H2Z,5H73,5HQE,5HIN,3KVJ,3KVL,5MUT,5MVC,5MVD,4JTU,4YLW,4ZL1,4ZMG,5ZF9,5ZF4,5ZF8,5ZF7,5ZFA,6GK0,5K9D,5K9C,6FMD,6QU7,6ET4,6LZL,6CJF,6OC0,6SYP,6IDJ,6J3B,6J3C,6JMD,6JME
#That is because these are human DHODH gene associated, have better resolution than 2.0A, obtained  after 2009, and present in asymetrical rather than cyclic

import os,subprocess

vina_executable=r"D:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe"
ligands_dir=r"ligands"
# receptors_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\4-14-20\receptors"
receptor_filename=r"5k9d.pdbqt"
receptors_dir="receptors"
max_deltaG=-11.0

config_filename=r"conf.txt"
results_dir=r"dockings"
EXHAUSTIVENESS= 16
OVERWRITE=False
ligands=[ x for x in os.listdir(ligands_dir) if x.endswith("pdbqt")]



# receptors=[ x for x in os.listdir(receptors_dir) if x.endswith("pdbqt")]


from summarize_results import read_summary
data=read_summary()

# exit()
# for receptor in receptors:

for ligand in ligands:
    print( ligand)
    print(max([float(x) for x in data[ligand.split(".")[0]].values() if x!=""])>=max_deltaG)
    b=(max([float(x) for x in data[ligand.split(".")[0]].values() if x!=""])>=max_deltaG)
    # b = (max([float(x) for x in data[ligand.split(".")[0]].values()]) >= max_deltaG)
    if b:
        print("skipping:",ligand)
        continue
    if not OVERWRITE and os.path.exists(results_dir+'/'+receptor_filename[:-6]+"_"+ ligand[:-6]+'.pdbqt'):
        print("skipping:", ligand, "It's docking pdbqt file exists.")
        continue

    config_file=open(config_filename,"w")
    config_file.write('ligand= "'+ligands_dir+'/'+ligand+'"\n')
    config_file.write('receptor= "'+receptors_dir+'/'+receptor_filename+'"\n')
    config_file.write('out= "'+results_dir+'/'+receptor_filename[:-6]+"_"+ ligand[:-6]+'.pdbqt"\n')
    config_file.write('log= "'+results_dir+'/'+receptor_filename[:-6]+"_"+ ligand[:-6]+'.txt"\n')
    config_file.write("center_x=34.569\n")
    config_file.write("center_y=-15.848\n")
    config_file.write("center_z=-18.938\n")
    config_file.write("size_x=18\n")
    config_file.write("size_y=28\n")
    config_file.write("size_z=22\n")
    config_file.write("exhaustiveness=" + str(EXHAUSTIVENESS))
    config_file.flush()
    config_file.close()

    command='"'+vina_executable+'"' +' --config '+'"'+config_filename+'"'
    # command=vina_executable +' --config '+config_filename
    print("command: "+command)
    subprocess.call(command)

