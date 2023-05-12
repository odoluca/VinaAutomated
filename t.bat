echo "WORKING..."

obabel 007_ideal.sdf -O 007_ideal.pdbqt -p
echo "first conversion doesnt apply charges to pH dependent hydrogens"
obabel 007_ideal.pdbqt -O 007_ideal.pdbqt --partialcharge gasteiger --seperate --unique
echo "second conversion calculates charges for pH dependent hydrogens too"
"D:\Program Files (x86)\MGLTools-1.5.6\python.exe" "D:\Program Files (x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_receptor4.py" -r "C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\structures\6gh0.pdb" -o "C:\Users\doluc\PycharmProjects\VinaAutomated\experiments\3-7-20_2\receptors\6gh0.pdbqt" -v
