# Project_SS
Projet_court_structure_secondaire

Setup you environment :

git clone git@github.com:maha652/Project_SS.git

Move to the new directory 

cd Project_SS

Install miniconda : 
https://docs.conda.io/en/latest/miniconda.html


Create the Projet_SS conda environment : 

$ conda env create -f env_mg_projet.yml

Load the  Projet_SS conda environment :

conda activate Project_SS

To deactivate an active environment , use : 

conda deactivate

Using the HBPLUS v.3.06 - a hydrogen bond calculation program

Go to the link :
https://www.ebi.ac.uk/thornton-srv/software/HBPLUS/

Ask for permission for academic use : 

complete the Confidentiality Agreement below
https://www.ebi.ac.uk/thornton-srv/software/HBPLUS/confid.txt

and post, fax or e-mail to Roman Laskowski (as given at the end of the agreement) to receive download instructions. 

Once the HBPLUS installed compile the programs by typing :

make

after that you have to write :
./hbplus 

After that the program will ask you to choose the directory name for output file and the name of the next file to be processed , for our protein test it will be for exemple ../1huf.pdb

Remark  : i already added a file generated thanks to HBPLUS for our protein test it will be 1huf.hb2



Runing

You should be ready to run the program , by calling for example :

python ss_mg_project.py

you should have your file extracted from HBPLUS  
( in our case  1huf.hb2 ) in the same repository with ss_mg_projet.py

Output :

A file called helices&feuillets.txt composed of six Columns.

column's identification 

a: 

amino acid position

kind :

abbreviation of the amino acid name

helix :

the helices formed ("H" to say helice)

turn: 
there are three types of turn
the turns formed are ( 3 , 4 , 5 )

Bridge: 

"B" presence of a  bridge in this position 

leader: 

"L" presence of a leader in this position 

sheet: 

"F" presence of a sheet in this position 





















