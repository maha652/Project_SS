#****************** Initialisation ********************************
helices = []
bridges = []
Hbond_pos = []
Hbond_deuxiemepos =  []
type = []                                   
num = []
turn = []                                                     
Hbond_final_tri_num = []                  
num_tri = []                               
leader = []
feuillet = []
resultat= ''
#****************** lire fichier hb2  ********************************
with open ("1huf.hb2" , "r") as Hydrongen :
    for line in Hydrongen :
        if line.startswith('A0') :
            line = line.split()
            Hbond_pos.append(line[0].split("-")[0][-4:])
            type.append(line[0].split("-")[1])
            Hbond_deuxiemepos.append(line[2].split("-")[0][-4:])
            num.append(line[12])

longueur = len(num)      
#****************** tri et création de la liste hbplus **************
i=1
for i in range(longueur) : 
    Hbond_final_tri_num+=[ [Hbond_pos[i] , Hbond_deuxiemepos [i]  , type[i]  ]  ]
    helices += ['-']
    bridges += ['-']          
    leader  += ['-']                     
    feuillet += ['-']       
Hbond_final_tri_num.sort()

for i in range (longueur) :
    type[i] = Hbond_final_tri_num[i][2]

    

  
      


# ******************  Fonction hélice ********************************

for i in range (longueur) :
    a = int (Hbond_final_tri_num[i][0])
    b = int (Hbond_final_tri_num[i][1])                               
    if abs(a - b)  == 3 :                          
        turn += [3]
    elif abs(a - b)  == 4 :
        turn += [4]
    elif abs(a - b)  == 5 :
        turn += [5]
    else :
        turn += ['-']
    
for i in range (longueur):
    if turn[i] == turn[i-1] and turn[i] in [3,4,5]  :   
        helices [i] = "H"
        helices [i-1] = "H"
        i=i+1

    

#************************Fonction feuillet ********************************
i=1
for i in range (longueur-1) :
    a = int (Hbond_final_tri_num[i][0])                     #    i-1    a1  3      b1 2012
    b = int (Hbond_final_tri_num[i][1])                     #     i     a   7      b  0004
    a1 = int (Hbond_final_tri_num[i-1][0])                  #    i+1    a2  8      b2 0005 / 0003
    a2 = int (Hbond_final_tri_num[i+1][0])
    b2 = int (Hbond_final_tri_num[i+1][1])
    if a1<a and a<a2 and a2-a == 1 and a - a1 == 1 :
        if abs (b-b2) == 1 :         # utliser le b de i+1
            bridges [i] = "B"

i=0
for i in range (longueur):
    if bridges[i] == "B" and bridges[i-1]== "B"  :   
        leader[i-1] = "L"
        i=i+1
i=0
for i in range (longueur):
    if leader[i] == "L" and leader[i-1]== "L" and feuillet[i-1] == '-' :   
        feuillet [i] = "F"
        feuillet[i-1] = "F"
        i=i+2

with open('feuillet.txt', 'w') as f:
        f.write("  feuillet")
        for i in range (longueur) :
            resultat = (str(feuillet))
        f.write(resultat)
    
#************************   Sortie en Terminal  *********************

print("       a        type     helice     turn     bridge    leader  feuillet")
for i in range (longueur) : 
    print("     " , Hbond_final_tri_num[i][0], "     " , type[i]  ,"     " ,helices[i],"         " , turn [i],"         " , bridges[i] ,"     ", leader[i] ,"      ", feuillet[i] )


with open('helices&feuillets.txt', 'w') as f:
    f.write("     a        type    helice   turn    bridge leader feuillet\n")
    for i in range (longueur) : 
        resultat = ("     " + str(Hbond_final_tri_num[i][0]) + "     " + str(type[i]) + "     " + str(helices[i]) + "         " + str(turn [i]) + "       " + str(bridges[i] ) + "       " + str(leader[i])  + "    " + str(feuillet[i])+"\n" )
        f.write(resultat)
        
