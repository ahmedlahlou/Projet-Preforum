import csv
import os




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
            
    def filt(self,listP,             
        listPB = []
        for k in range(len(listP)):
            if (listP[k].lch[i] == 1):
                listPB . append(listP[k])
        return listPB
        




def searchacti(code,actis):
    k = 0
    for i in range len(actis):
        if code == actis[i].code:
            k = i
    return k
    
def zeros(k):
    t = []
    for i in range(k):
        t.append(0)
    return t
        
        

#structure provisoire du programme



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


    
    
    


