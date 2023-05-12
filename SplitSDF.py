import sys,os
input_filename=r"D:\Users\doluc\Downloads\drugbank_all_3d_structures\3D structures.sdf"
min_complexity_threshold=200.0
min_heavyatom_count_threshold=15
max_TPSA_threshold=999999.0
min_TPSA_threshold=100.0

if len(sys.argv)==0 and input_filename=="":
    input_filename=input("Enter sdf file to be splitted>>>")

assert os.path.isfile(input_filename), "input file is not found."
assert input_filename.endswith(".sdf"),".sdf extention is required."
directory= os.path.dirname(input_filename)

counter=0
with open(input_filename,"r") as f:
    content=""
    new_sdf=True
    new_complexity=False
    new_sdf_complexity=0
    new_heavyatom_count=False
    new_sdf_heavyatom_count=0
    new_TPSA=False
    new_sdf_TPSA=0

    for line in f.readlines():

        content+=line

        if new_complexity:
            new_complexity=False
            new_sdf_complexity=float(line.strip("\n "))
        if line.__contains__("PUBCHEM_CACTVS_COMPLEXITY"):
            new_complexity=True #next line will contain complexity

        if new_heavyatom_count:
            new_heavyatom_count=False
            new_sdf_heavyatom_count=int(line.strip("\n "))
        if line.__contains__("PUBCHEM_HEAVY_ATOM_COUNT"):
            new_heavyatom_count=True

        if new_TPSA:
            new_TPSA=False
            new_sdf_TPSA=float(line.strip("\n "))
        if line.__contains__("PUBCHEM_CACTVS_TPSA"):
            new_TPSA=True

        if new_sdf and line.strip("\n ") != "":
            new_sdf = False
            new_sdf_title = line.strip("\n ")
        if line.startswith("$$$$"):
            new_sdf=True #next line will contain new sdf title
            counter+=1
            # print(counter)
            if new_sdf_complexity>=min_complexity_threshold and new_sdf_heavyatom_count>=min_heavyatom_count_threshold and (min_TPSA_threshold<=new_sdf_TPSA<=max_TPSA_threshold) :
                # print("",new_sdf_title,new_sdf_complexity,new_sdf_heavyatom_count,new_sdf_TPSA)
                # # BELOW CREATES FILES
                # with open(directory+"\\"+new_sdf_title+".sdf","w") as n:
                #     n.write(content)
                print(new_sdf_title,end=",")
            new_sdf_complexity=0.0
            new_sdf_heavyatom_count=0
            new_sdf_TPSA=0.0
            content=""



