import subprocess,os
# split_py=r"D:\\Program Files (x86)\\MGLTools-1.5.6\\Lib\\site-packages\\AutoDockTools\\Utilities24\\prepare_pdb_split_alt_confs.py"
prepare_py=         r"D:\\Program Files (x86)\\MGLTools-1.5.6\\Lib\\site-packages\\AutoDockTools\\Utilities24\\prepare_ligand4.py"
python_exec=        r"D:\\Program Files (x86)\\MGLTools-1.5.6\\python.exe"
pdb_dir=            r"C:\\Users\\doluc\\PycharmProjects\\VinaAutomated\\experiments\\4-14-20\\ligands"

target_pdbqt_dir=   r"C:\\Users\\doluc\\PycharmProjects\\VinaAutomated\\experiments\\4-14-20\\ligands"


pdbs=[ x for x in os.listdir(pdb_dir) if x.endswith("pdb")]
for pdb in pdbs:


    # command='"'+python_exec+'" "'+prepare_py+'" -l "'+pdb_dir+'\\'+pdb  +'" -o '+'"'+ target_pdbqt_dir+'\\'+pdb+'qt -v"'
    command = '"'+python_exec + '" "'+   prepare_py + '" -l "' + pdb_dir + r'\\' + pdb + '" -o "' +  target_pdbqt_dir + r'\\' + pdb + 'qt" -v '
    print("command:"+command)
    subprocess.call(command,shell=True)
    # subprocess.call([python_exec,prepare_py,"-r",pdb_dir+'\\'+pdb,"-o",target_pdbqt_dir+'\\'+pdb+'qt"pre',"-v"],shell=True)


