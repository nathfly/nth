"""a=input ("combien de millilitres de sang il y a-t-il dans l'echantillon? ")
a=int(a)
b=input ("combien de vitamine d il y a-t-il dans l'echantillon? ")
b=int(b)
Formule =( b / a )
if Formule <=10:
    print ("Le taux de Vitamine D est deficiente")
elif Formule <=30:
     print ("Le taux de vintamine D est insuffisante")
elif Formule <=100:
     print ("Le taux de vitamine D est suffisante")
else:
     if Formule >100:
        print("Le taux de vitamine D est excessive")

"""


a=input ("Est-ce que ta forme a quelque chose a l'interieur d'elle?  ")
if a=="oui":
   a1 = input("Est-ce que ta forme a une croix a l'interieur? ")
   if  a1 =="oui":
        a2=input ("Ta forme est elle de couleur verte? ")
        if  a2=="oui":
            print("Ta forme est le pentagone vert ")
        else:
              print ("Ta forme est le pentagone couleur orange avec la croix a l'interieur ")
   else : 
        a3= input ("Est ce que ta forme est de couleur bleu? ")
        if  a3=="oui":
               print("Ta forme est le carre bleu avec la photo de Shakira a l'interieur")
        else:
            print("Ta forme est le carre rouge avec le rond a l'interieur")
            
        
else :
    b=input (" Est-ce que le nombre de cotés de ta forme est un chiffre pair? ")
    if b== "oui" :
       b1= input (" Ta forme est-elle rouge? ")
       if b1== "oui":
            print(" Ta forme est l'hexagone rouge") 
       else:
            print("Ta forme est l'hexagone bleu ")
    else:
        b2=input("Ta forme est elle jaune? ")
        if b2== "oui":
                print("Ta forme est le trialngle jaune ")
        else:
            print("Ta forme est le triangle vert")
     
     
     
     

aa=input ("Est-ce que ta forme a un point a l'interieur d'elle?  ")
if aa=="oui":
   aa1 = input("Est-ce que ta forme a une couleur rouge ")
   if  aa1 =="oui":
        aa2=input(" Est-ce que le nombre de cotés de ta forme est un chiffre pair? ")
        if  aa2=="oui":
            print("Ta forme est le carré rouge")
        else:
              print ("Ta forme est le pentagone rouge")
   else : 
        aa3= input (" Est-ce que le nombre de cotés de ta forme est un chiffre pair? ")
        if  aa3=="oui":
               print("Ta forme est le carré bleu ")
        else:
            print("Ta forme est le  pentagone bleu ")
            
        
else :
    bb=input (" Est-ce que le nombre de cotés de ta forme est un chiffre pair? ")
    if bb== "oui" :
       bb1= input (" Ta forme est-elle rouge? ")
       if bb1== "oui":
            print(" Ta forme est l'hexagone rouge") 
       else:
            print("Ta forme est l'hexagone bleu ")
    else:
        bb2=input("Ta forme est elle rouge? ")
        if bb2== "oui":
                print("Ta forme est le trialngle rouge ")
        else:
            print("Ta forme est le triangle bleu")
     
     
  