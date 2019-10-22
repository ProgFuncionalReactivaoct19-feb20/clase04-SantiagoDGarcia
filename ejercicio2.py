"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
listaA = [(100, 2), (20, 4), (30,1)]
listaB = ["b", "a", "c"]

#Se ordena y se desordena las listas B y A respectivamente
"""
Version 1
listaA2 = sorted(listaA, key=lambda x: x[1])
listaB2 = sorted(listaB)
"""
# Se imprime en una lista 
print(list(zip(sorted(listaB),sorted(listaA, key=lambda x: x[1]))))

