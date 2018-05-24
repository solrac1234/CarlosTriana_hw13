import random
import numpy as np 
a= True
b= False

# esta funciom retorna una lista aleatoria  

def sort_doors():

	lista_aleatoria = ['goat','goat','car']
	random.shuffle(lista_aleatoria)
	return lista_aleatoria 
	
print sort_doors(),  "[lista aleatoria]"



# Funcion que retorna un numero aleatorio entre 0 y 2

def choose_door():

	lista = [0,1,2]
	aleatorio = np.random.choice(lista)
	return aleatorio

print "SE ESCOJE LA PUERTA", choose_door()

# Recorre la lista en los espacios que no incluyen a choice , cuando encuentra el primer 'goat' lo remplaza por 'GOAT_MONTY'

def reveal_door(lista, choice):

	for i in range (len(lista)):
		if ((lista[i] =='goat') & (choice != i)):
			lista[i] = 'GOAT_MONTY'
			return lista

print reveal_door(sort_doors(), choose_door())

def azar():

	a= True;b= False	
	list = [a, b]
	randbool = np.random.choice(list)
	return randbool


def finish_game(lista,choice,change):

	for i in range (len(lista)):
		if ((change == a) & (lista[i] != 'GOAT_MONTY') & (lista[i] != lista[choice])):
			return lista[i]
		else:
			return lista[choice]
print finish_game(sort_doors(), choose_door(),True);print finish_game(sort_doors(), choose_door(),False);print finish_game(sort_doors(), choose_door(),azar())

	

verdadero=[];falso=[]

for i in range(100): 

	n = choose_door()	

	verdadero.append(finish_game(reveal_door(sort_doors(), n), n , True))
	
	falso.append(finish_game(reveal_door(sort_doors(), n), n , False))	

A = 0 ; B= 1

for i in range (len(verdadero)): 
	if(verdadero[i] == "car"):
		A= A+B  	
print "la probabilidad de ganar cambiando de puerta sera  ", A,"porciento"

C = 0 

for i in range(len(falso)):

	if(falso[i] == "car"):
		C = C+B
print "la probabilidad de ganar sin cambiar de puerta es  ", C,"porciento"
