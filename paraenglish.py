
"""a=input("Combien d'heures se sont ecoulées? ")
b=input("Combien de minutes se sont écoulées? ")
c=input("Combien de secondes se sont écoulées? ")
a=int(a)
b=int(b)
c=int(c)
a1=(a*3600)
b1=(b*60)
c11=(c*1)
print((c11)+(b1)+(a1))
"""


F=input("Combien de secondes se sont ecoulees? ")

def seconde(F):
heure = F // 3600
    minute = (F - (3600*heure))//60
    secondes = F-(3600*heure)-(60*minute)
    time = (heures, minutes, secondes)
    return time

resultat = (seconde(456))
print("% heures, % minutes et % secondes\n" %(resultat[0], resultat[1], resultat[2]))
