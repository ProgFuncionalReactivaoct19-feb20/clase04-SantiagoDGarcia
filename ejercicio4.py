"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

prom = lambda x: (x[0]+ x[1]+ x[2])/3
prom2 = list(map(prom, paraleloA))

print(list(zip(prom2,nombres)))



