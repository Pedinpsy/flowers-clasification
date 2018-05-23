import csv
import random as rd
def dist_euclidiana(v1, v2):
	dim, soma = len(v1)-1, 0
	for i in range(dim):
		soma += math.pow(v1[i] - v2[i], 2)
	return math.sqrt(soma)
data = []
teste = []
with open ('iris.data', newline='') as csvfile:
  lines = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in lines:
    data.append(row)
  data.pop()
  rd.shuffle(data)
  
  for i in range(0,round(len(data)/3)):
    teste.append(data[i])
    data.remove(data[i])
  for aux in teste:
    print(aux)
 
    
  
