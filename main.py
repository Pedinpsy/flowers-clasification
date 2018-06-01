import csv
import random as rd
import math
from operator import itemgetter


class planta:
        def __init__(self,nome):
                self.nome = nome
                vp = 0
                fp = 0
                fn = 0
                vn = 0
        
def dist_euclidiana(v1, v2):
        dim, soma = len(v1)-1, 0
        for i in range(dim):
                soma += math.pow(float(v1[i]) - float(v2[i]),2)
        return math.sqrt(soma)
def predicao(data,n):
        versicolor = 0
        setosa = 0
        virginica = 0
        for i in range(0,n):
                print(data[i])
                if data[i][1] == 'Iris-setosa':
                        setosa+=1
                elif data[i][1] == 'Iris-virginica' :
                        virginica+=1
                else :
                        versicolor+=1
        if versicolor > setosa and versicolor > virginica:
                return 'Iris-versicolor'
        elif setosa > versicolor and setosa> virginica:
                return 'Iris-setosa'
        else :
                return 'Iris-virginica'
                
                
data = []
teste = []
with open ('iris.data', newline='') as csvfile:
        n = 5
        versicolor = planta("versicolor")
        setosa = planta("setosa")
        virginica = planta("virginica")
        lines = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in lines:
                data.append(row)
        data.pop()
        rd.shuffle(data)
        
        for i in range(0,round(len(data)/10)):
                teste.append(data[i])
                data.remove(data[i])

        euclidian = []        
        for aux in data:
                print(aux)
                
        for aux in teste:
                for auxData in data:
                        euclidian.append([dist_euclidiana(aux,auxData),auxData[4]])
                euclidian.sort(key=itemgetter(0))
                aux.append(predicao(euclidian,n))
                euclidian = []
        for item in teste:
                if item[4] != item[5] :
                	print("errado") 
       


                
                       
 
