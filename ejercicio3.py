"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
listaA = [(100, 2), (20, 4), (30,1)]
listaB = ["b", "a", "c"]

listaB1 = lambda x: x.upper()

print(list(zip(sorted(listaB), sorted(listaA, key=lambda x:[1]))))

