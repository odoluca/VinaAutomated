import os,subprocess

vina_executable=r"D:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe"
ligands_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\7-13-20\ligands"
receptors_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\7-13-20\receptors"
config_filename=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\7-13-20\conf.txt"
results_dir=r"C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\7-13-20\dockings"

ligands=[ x for x in os.listdir(ligands_dir) if x.endswith("pdbqt")]
receptors=[ x for x in os.listdir(receptors_dir) if x.endswith("pdbqt")]

# exhaustiveness= 8

for receptor in receptors:
    for ligand in ligands:


        config_file=open(config_filename,"w")
        config_file.write('ligand= "'+ligands_dir+'/'+ligand+'"\n')
        config_file.write('receptor= "'+receptors_dir+'/'+receptor+'"\n')
        config_file.write('out= "'+results_dir+'/'+receptor[:-6]+"_"+ ligand[:-6]+'.pdbqt"\n')
        config_file.write('log= "'+results_dir+'/'+receptor[:-6]+"_"+ ligand[:-6]+'.txt"\n')
        config_file.write("center_x=14.78\n")
        config_file.write("center_y=20.976\n")
        config_file.write("center_z=8.807\n")
        config_file.write("size_x=18\n")
        config_file.write("size_y=18\n")
        config_file.write("size_z=40\n")
        config_file.write("exhaustiveness=64")
        config_file.flush()
        config_file.close()

        command='"'+vina_executable+'"' +' --config '+'"'+config_filename+'"'
        # command=vina_executable +' --config '+config_filename
        print("command: "+command)
        subprocess.call(command)

