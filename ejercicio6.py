"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]

prom = list(map(lambda x: (x[0]+ x[1]+ x[2])/3, paraleloA))


#Otra forma de evaluar...
def eval(x):
	if x <=5:
		return True
	else:
		return False
funPro = filter(eval, prom)

add = list(map(lambda x: (x[0]+ x[1]+ x[2]), paraleloA))
def suma(x):
	if x <= 15:
		return True
	else:
		return False
funSum = filter(suma, add)

def eval2(x):
	if x[0]=="Á" or x[0]=="A":
		return True
	else:
		return False
funName = filter(eval2, nombres)

print(list(zip(funPro, funSum, funName)))