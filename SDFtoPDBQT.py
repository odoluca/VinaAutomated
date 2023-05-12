#SERIAL CONVERSION OF SDF FILES INTO PDBQT FILES
import sys
import os
import subprocess
"""
The program requires a all SDF files in a specific folder and with .sdf extention. Other extentions or formats are not allowed.
The program requires openbabel installed
The program assumes 3d coordinates are already generated.
The program calculates hydrogens for pH 7. and calculates gasteiger charges.
"""
source_folder=r'C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\DHODHs2\ligands'
target_folder= None
for idx,arg in enumerate(sys.argv):
    if arg=='-M':
        source_folder=input('enter source folder >>>').strip('\\')+'\\'
        assert os.path.isdir(source_folder),'source folder does not exist. Use " if necessary'

        source_folder = input('enter target folder >>>').strip('\\') + '\\'
        assert os.path.isdir(source_folder), 'target folder does not exist. Use " if necessary'

    if arg=='-S':
        try:
            source_folder=sys.argv[idx+1].strip(' \\')+'\\'
        except:
            exit('Please enter source directory after -S')
        assert os.path.isdir(source_folder), 'source folder does not exist. Use " if necessary'

    if arg=='-T':
        try:
            target_folder=sys.argv[idx+1].strip(' \\')+'\\'
        except:
            exit('Please enter target directory after -T')
        assert os.path.isdir(target_folder), 'target folder does not exist. Use " if necessary'
print("Source:",source_folder)
if target_folder==None: target_folder=source_folder
print("Target:", target_folder)


if __name__=='__main__':
    #TODO: Find all sdf files
    #TODO: convert them to PDBQT with -p options
    #TODO: reconvert them to calculate gasteiger charges


    for sdf_filename in [ x for x in os.listdir(source_folder) if x.endswith(".sdf")]:
        pdbqt_filename=sdf_filename[:-3]+"pdbqt"
        # command = "obabel " + source_folder + "\\" + sdf_filename + " -O " + target_folder + "\\" + sdf_filename + " --gen3d 1"
        # subprocess.call(command)
        command= "obabel "+source_folder+"\\"+sdf_filename+" -O "+target_folder+"\\"+pdbqt_filename +" -p -r" # -r for keeping only biggest fragment, -p for placing pH7 hydrogens
        print(command)
        subprocess.call(command)
        command = "obabel " + target_folder+"\\"+pdbqt_filename + " -O " + target_folder +"\\"+ pdbqt_filename + " --partialcharge gasteiger --seperate --unique"
        subprocess.call(command)
        print("\tconverting:",sdf_filename,"-->",pdbqt_filename)

