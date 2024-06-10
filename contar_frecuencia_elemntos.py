
l=[1,2,4,5,4,6,6,4]

s={1:1,2:1,4:3,5:1,6:2}

from collections import Counter

def contar_frecuencia(lista):
    return dict(Counter(lista))

lista=["manzana","pera","manzana","uva","uva"]
frecuencias= contar_frecuencia(lista)
#print(contar_frecuencia(frecuencias))

elementos_unicos=list(set(lista))
elementos_unicos_str= " ".join(elementos_unicos)
print(f"Los elemntos de la lista  son: {elementos_unicos_str}")

a=input("Introduce un elemento que quieras saber la frecuencia: ")
print(f"La frecuencia de {a} es: {frecuencias[a]}")





