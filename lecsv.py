import csv
import os
import random



class person(object):
    #temps à mettre ici
    def __init__(self,name,lastname,lch,promo):
        self.name = name
        self.lastname = lastname
########### MODIFICATION IMPORTANTE, LCH RENFERME LES INDICES DES TACHES CHOSIIES ET NON PLUS DES 001100// PAS FORCEMENT
        self.lch = lch
        self.lres = zeros(len(lch))
        self.promo = promo

        
class acti(object):
    def __init__(self,entreprise,intNom,intPrenom,creneau,type,capacity):
        self.type = type
        self.entreprise = entreprise
        self.intNom = intNom
        self.intPrenom = intPrenom
        self.creneau = creneau
        #self.tabIndice= []
        
        #self.code = code
        self.capacity = capacity
        self.listPrincipale = []
        self.listAttente = []
        #self.tabIndice = tabIndice
        
    def genereCode(self):
        #generation de code
        code = self.entreprise[0]+self.entreprise[1]+self.intNom[0]+self.intNom[1]+self.intPrenom[0]
        #partie créneau
        cre = stringToList(self.creneau)
        i = cre.index(":")
        code = code + cre[0] + cre[1] + cre[i-2]+cre[i-1]+cre[i+1]+cre[i+2]
        i = cre.index("(")
        code = code + cre[i+1] + cre[i+2]
        self.code = code
        
        
class solver(object):
    
    def __init__(self, listP, listA, mat):
        self.listP = listP
        self.listA = listA
        self.mat = mat 
        
    def solve(self):
        
        listP = self.listP
        listA = self.listA
        mat = self.mat
        
        #on parcoure chaque tâche séparément
        for i in range(len(listA)):
            task = listA[i]
            self.calcscore(task,listP)
            listelig = self.filt(listP,i)
            for j in range(task.capacity):
                task.listPrincipale.append(listelig[j])
                k = listP.index(listelig[j])
                listP[k].lres[i] = 1
                
            #liste d'attente à trier aussi !!!!!!!
            task.listAttente = listelig[task.capacity+1:]
            
        #tri de liste d'attente 
        for i in range(len(listA)):
            task = listA[i]
            self.calcscore(task,task.listAttente)
            
        
        
    def calcscore(self,task,liste):
        listP = liste
        type = task.type
        score = []
        
        # Calcul du score de chaque étudiant 
        for i in range(len(listP)):
            score.append(self.calcscoreP(listP[i],type))
        
        # Tri de la liste d'étudiants
        #PARTIE A MODIFIER POUR INCORPORER LA GESTION DU TEMPS
        
        for i in range(len(listP)):
            k = i
            for j in range(i+1,len(listP)):
                if (score[k]>score[j]):
                    k = j
                score[k], score[j] = score[j], score[k] 
                listP[k],listP[j] = listP[j],listP[k]
                
    def calcscoreP(self, personE, type):
        lres = personE.lres
        listT = self.listA
        value = 0
        for i in range(len(lres)):
            if (lres[i] == 1):
                value = value + self.mat[type][listT[i].type]
        return value
            
    def filt(self,listP,i):             
        listPB = []
        for k in range(len(listP)):
            if (listP[k].lch[i] == 1):
                listPB . append(listP[k])
        return listPB
        
    def comparetime(self,time1,time2):
        #temps au format hh:mm
        #temps sous fore de string
        #Si la fonction retourne 1 ca veut dire que time1 > time2
        
        if (int(time1[0]+time1[1]) > int(time2[0]+time2[1])):
            return 1
        elif (int(time1[0]+time1[1]) == int(time2[0]+time2[1])):
            if (int(time1[3]+time1[4]) >= int(time2[3]+time2[4])):
                return 1
            else:
                return 0
        else:
            return 0
            
        
def stringToList(string):
    r = []
    for i in range(len(string)):
        r.append(string[i])
    
    return r
    


def searchacti(code,actis):
    k = -1
    for i in range (len(actis)):
        if code == actis[i].code:
            k = i
    return k
    
def searchPerson(name,lastname,personnes):
    k = -1
    for i in range(len(personnes)):
        if (name == personnes[i].name):
            if (lastname == personnes[i].lastname):
                k = i
    return k
        
def zeros(k):
    t = []
    for i in range(k):
        t.append(0)
    return t
    
def separate(list):
    r = ""
    res = []
    chaine = list[0]
    for i in range (len(chaine)):
        if (chaine[i] != ";"):
            r = r + chaine[i]
        else:
            res.append(r)
            r = ""
            
    return res
        

#structure provisoire du programme



#################PARTIE LECTURE DU FICHIER EXCEL


"""
les actis et les personnes sur un seul et même excel
colonnes pour actis : nom entreprise / nom et prénom de l'entreprise / créneau / Dpp
nomenclature pour les actis : 
Colonnes pour les personnes : Etuduant Nom / Etudiant prénom / Etudiant promo / Date et heure du Shotgun / numero de tel

"""




#importation de l'excel avec les actis

os.chdir("C:/Users/Ahmed/Desktop/Projetpreforum")
cr = csv.reader(open("export_2015.csv","r"))

fichierEx = []

types = ["Discussion projet professionnel","Correction de CV en Français","Correction de CV en Anglais","Simulation d'entretien en Français","Correction de lettre de motivation","Simulation d'entretien en Anglais"]



for row in cr :
    fichierEx.append(row)

intermed = []
    
for i in range (len(fichierEx)):
    fichierEx[i] = separate(fichierEx[i])
    

    
listT = []
listP = []


for i in range(1,len(fichierEx)):
    
    #d'abord une nomenclature ++ ajout dans la classse d'un tableau avec les lignes de l'activité ++ liste de tute les nomenclatures , risque de doublon ? 
    tache = acti(fichierEx[i][0],fichierEx[i][1],fichierEx[i][2],fichierEx[i][3],types.index(fichierEx[i][9]),1) ### capacité provisoire !!
    tache.genereCode()
    if(i == 368):
        print(tache.code)
    
    if (searchacti(tache.code,listT) == -1):
        listT.append(tache)
        k = len(listT) - 1 
    else:
        k = searchacti(tache.code,listT)
        #listT[k].tabIndice.append(k)
        print(k,i)
    
    # partie persones
    lch = zeros(len(fichierEx))
    perso = person(fichierEx[i][5],fichierEx[i][6],lch,fichierEx[i][7])
    
    if (searchPerson(fichierEx[i][5],fichierEx[i][6],listP) == -1):
        listP.append(perso)
        h = len(listP)-1
    else:
        h =  searchPerson(fichierEx[i][5],fichierEx[i][6],listP)
        
    listP[h].lch[k]= 1
    if (i == 200):
        print(h,k)
   

for i in range(len(listP)):
    listP[i].lch = listP[i].lch[:len(listT)]



    


################################################

"""
mat = [[10,5,2],[5,10,2],[5,2,10]]

alph = ["a","b","c","d","e","f","g","h","i"]



#PARTIE TEST !!!
# on genere 100 personnes aléatoires -- avec 10 actis -- dont 3 types

listP = []
listT = []

for i in range (100):
    nom = alph[random.randint(0,8)] + alph[random.randint(0,8)] + alph[random.randint(0,8)]
    lch = []
    for i in range (10):
        lch.append(random.randint(0,1))
    listP.append(person(nom,"",lch))
    
#personnes générées

listT.append(acti("AZE",0,1))
listT.append(acti("AZR",0,10))
listT.append(acti("AZF",1,5))
listT.append(acti("AZK",1,3))
listT.append(acti("AZA",2,1))
listT.append(acti("BZE",0,7))
listT.append(acti("BZR",0,8))
listT.append(acti("BZF",1,9))
listT.append(acti("BZK",1,1))
listT.append(acti("BZA",2,1))

solvera = solver(listP,listT,mat)

solvera.solve()

for i in range(10):
    print(listT[1].listPrincipale[i].name, listT[1].listPrincipale[i].lch)

#pourcentage de personnes ? 

#PROGRAMME CORRECTEMENT DEBUGUE
#INCORPORER TEMPS 
"""

#######Pour le reste :
"""
our chaque choix, affecter la ligne dans l'excel correspondante, si e choix refusé, supprimer tout simplement la ligne 

"""