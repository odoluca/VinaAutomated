import os,subprocess,sys

vina_executable=r"D:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe"
ligands_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\DHODH_DrugBank_ligands\ligands"
receptors_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments/DHODH_DrugBank_ligands\receptors"
# config_filename=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments/Spike_3_28_20\conf.txt"
results_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments/DHODH_DrugBank_ligands\dockings"

ligands=[ x for x in os.listdir(ligands_dir) if x.endswith("pdbqt")]
receptors=[ x for x in os.listdir(receptors_dir) if x.endswith("pdbqt")]

# EXHAUSTIVENESS= 32

for receptor in receptors:
    for ligand in ligands:
        config_filename=receptor[:-5]+"_conf.txt"
        # assert os.path.isfile(receptors_dir+'/'+config_filename), "Cannot find receptor-associated config file. Expected "+config_filename
        config_file=open(config_filename,"w")
        config_file.write('ligand= "'+ligands_dir+'/'+ligand+'"\n')
        config_file.write('receptor= "'+receptors_dir+'/'+receptor+'"\n')
        config_file.write('out= "'+results_dir+'/'+receptor[:-6]+"_"+ ligand[:-6]+'.pdbqt"\n')
        config_file.write('log= "'+results_dir+'/'+receptor[:-6]+"_"+ ligand[:-6]+'.txt"\n')
        config_file.write("center_x=34.569\n")
        config_file.write("center_y=-15.848\n")
        config_file.write("center_z=18.938\n")
        config_file.write("size_x=18\n")
        config_file.write("size_y=28\n")
        config_file.write("size_z=22\n")
        config_file.write("EXHAUSTIVENESS=16")
        config_file.flush()
        config_file.close()

        command='"'+vina_executable+'"' +' --config '+'"'+config_filename+'"'
        # command=vina_executable +' --config '+config_filename
        print("command: "+command)
        subprocess.call(command)

