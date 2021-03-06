import csv
import os
import random



class person(object):
    def __init__(self,name,lastname,lch):
        self.name = name
        self.ladtname = lastname
        self.lch = lch
        self.lres = zeros(len(lch))

        
class acti(object):
    def __init__(self,code,type,capacity):
        self.type = type
        self.code = code
        self.capacity = capacity
        self.listPrincipale = []
        self.listAttente = []
        
        
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
            
        



def searchacti(code,actis):
    k = 0
    for i in range (len(actis)):
        if code == actis[i].code:
            k = i
    return k
    
def zeros(k):
    t = []
    for i in range(k):
        t.append(0)
    return t
        

#structure provisoire du programme

"""

#################PARTIE LECTURE DU FICHIER EXCEL


#importation de l'excel avec les actis

os.chdir("C:/Users/Ahmed/Desktop/Projetpreforum")
cr = csv.reader(open("actis.csv","r"))

acticsv = []

percsv=[]
for row in cr :
    acticsv.append(row)
    
actis = []

for i in range(len(acticsv)):
    activity = acti(acticsv[i][0],acticsv[i][1],acticsv[i][2])
    actis.append(activity)
    
#############Constante
Nbact = len(actis)
#############



        
#importation de l'excel du choix des personnes

os.chdir("C:/Users/Ahmed/Desktop/Projetpreforum")
cr = csv.reader(open("persons.csv","r"))

percsv=[]
for row in cr :
    percsv.append(row)
    
persons=[]
    
for i in range(len(percsv)):
    list = zeros(Nbact)
    for j in range(2,len(percsv[i])):
        indice = searchacti(percsv[i][j],actis)
        list[indice]=1
    personne = person(percsv[i][0],percsv[i][1],list)
    persons.append(personne)
    
print("liste de personnes et d'activités initialisée")

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
    


