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
            self.calcscore(task)
            listelig = self.filt(listP,i)
            for j in range(task.capacity):
                task.listPrincipale.append(listelig[j])
                k = listP.index(listelig[j])
                listP[k].lres[i] = 1
                
            #liste d'attente à trier aussi !!!!!!!
            task.listAttente = listelig[capacity+1:]
            
                
        
    def calcscore(self,task):
        listP = self.listP
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
                listP[k],list[j] = listP[j],listP[k]
                
    def calcscoreP(self, personE, type):
        listR = personE.lres
        listT = self.listT
        value = 0
        for i in range(lres):
            if (lres[i] == 1):
                value = value + self.mat[type][list[i].type]
        return value
            
    def filt(self,listP):             
        listPB = []
        for k in range(len(listP)):
            if (listP[k].lch[i] == 1):
                listPB . append(listP[k])
        return listPB
        




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

    
    


