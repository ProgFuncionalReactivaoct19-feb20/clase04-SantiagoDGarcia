"""
	Ejercicios clase04
	@SantiagoDGarcia
"""
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]
#Se ordena y se desordena las listas A y B respectivamente
listaA2 = sorted(listaA)
listaB2 = sorted(listaB, reverse=True)
# Se imprime en una lista y se imprime el maximo
print(list(zip(listaA2,listaB2)))
print(list(max(zip(listaA2,listaB2))))
