

import itertools
def generar_permutaciones(lista):
    return list(itertools.permutations(lista))

lista=[1,5,9,1]


permutacines=generar_permutaciones(lista)

for p in permutacines:
    print(p)