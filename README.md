# Big Papi reference file generation 
<b>This script helps generate reference files with all possible combinations of constructs for Big Papi screens</b><br/>
<b>Author</b>: Mudra Hegde  
<b>Email</b>: mhegde@broadinstitute.org  
<b>Version: 1.0 </b> 

<b>Required packages</b>
1. pandas

<b>Inputs</b><br/>
<b>Reference File 1</b>: .csv file with first column containing construct sequences and second column with construct IDs;no header<br/>
<b>Reference File 2</b>: .csv file with first column containing construct sequences and second column with construct IDs;no header<br/>
<b>Output File</b><br/>

<b>To run this script, type the following on the terminal:</b><br/>
python create_poolq_combo_ref_v1.0.py --ref1 \<Path to reference file 1\> --ref2 \<Path to reference file 2\> --outputfile \<.txt output file name\> 
