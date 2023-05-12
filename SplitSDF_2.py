import sys,os
input_filename=r"D:\Users\doluc\Downloads\drugbank_all_3d_structures\3D_structures.sdf"
# min_complexity_threshold=200.0
# min_heavyatom_count_threshold=15
# max_TPSA_threshold=999999.0
# min_TPSA_threshold=100.0

if len(sys.argv)==0 and input_filename=="":
    input_filename=input("Enter sdf file to be splitted>>>")

assert os.path.isfile(input_filename), "input file is not found."
assert input_filename.endswith(".sdf"),".sdf extention is required."
directory= os.path.dirname(input_filename)

counter=0
with open(input_filename,"r",encoding="utf8") as f:
    content=""
    new_sdf=True
    new_complexity=False
    new_sdf_complexity=0
    new_heavyatom_count=False
    new_sdf_heavyatom_count=0
    new_TPSA=False
    new_sdf_TPSA=0
    new_RO5=False
    new_sdf_RO5=False

    TITLE="DRUGBANK_ID"
    new_title=False
    new_sdf_title=""

    new_approved=False
    new_sdf_approved=False

    for line in f.readlines():

        content+=line

        # if new_complexity:
        #     new_complexity=False
        #     new_sdf_complexity=float(line.strip("\n "))
        # if line.__contains__("PUBCHEM_CACTVS_COMPLEXITY"):
        #     new_complexity=True #next line will contain complexity

        # if new_heavyatom_count:
        #     new_heavyatom_count=False
        #     new_sdf_heavyatom_count=int(line.strip("\n "))
        # if line.__contains__("PUBCHEM_HEAVY_ATOM_COUNT"):
        #     new_heavyatom_count=True

        # if new_TPSA:
        #     new_TPSA=False
        #     new_sdf_TPSA=float(line.strip("\n "))
        # if line.__contains__("PUBCHEM_CACTVS_TPSA"):
        #     new_TPSA=True

        if new_RO5:
            new_RO5=False
            new_sdf_RO5=(line.strip("\n ")=="1")
        if line.__contains__("JCHEM_RULE_OF_FIVE"):
            new_RO5=True

        if new_title:
            new_title=False
            new_sdf_title=line.strip("\n ")
        if line.__contains__("DRUGBANK_ID"):
            new_title=True

        if new_approved:
            new_approved=False
            new_sdf_approved=(line.__contains__("approved"))
        if line.__contains__("DRUG_GROUPS"):
            new_approved=True

        if new_sdf and line.strip("\n ") != "":
            new_sdf = False
            # new_sdf_title = line.strip("\n ")

        if line.startswith("$$$$"):
            new_sdf=True #next line will contain new sdf title
            # counter+=1
            print(counter,new_sdf_RO5,new_sdf_title,new_sdf_approved)
            # if new_sdf_complexity>=min_complexity_threshold and new_sdf_heavyatom_count>=min_heavyatom_count_threshold and (min_TPSA_threshold<=new_sdf_TPSA<=max_TPSA_threshold) :
            if new_sdf_title!="" and new_sdf_approved:
                # print("",new_sdf_title,new_sdf_complexity,new_sdf_heavyatom_count,new_sdf_TPSA)
                # BELOW CREATES FILES
                # with open(directory+"\\"+new_sdf_title+".sdf","w",encoding="utf8") as n:
                #     n.write(content)
                # print(new_sdf_title,end=",")
                counter+=1
                pass

            new_sdf_complexity=0.0
            new_sdf_heavyatom_count=0
            new_sdf_TPSA=0.0
            new_sdf_RO5=False
            new_title=""
            content=""
    print()
    print(counter,"drugs files created.")



