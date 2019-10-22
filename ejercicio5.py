"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
# Se crea funciones
prom = lambda x: (x[0]+ x[1]+ x[2])/3
prom2 = list(map(prom, paraleloA))
#Se contanena la lista
Lfin = list(zip(prom2,nombres))
# Se da la vuelta y se imprime
Lfin.reverse()
print(list(Lfin))
