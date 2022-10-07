from random import randint

def aleatorio(valor):
    return randint(0, valor)

vetor = list()
vetorI = list()
vetorP = list()


for i in range(30):
    vetor.append(aleatorio(1000))

for i in range(len(vetor)):
    if vetor[i]%2 == 0:
        vetorP.append(vetor[i])
    else:
        vetorI.append(vetor[i])

print(vetor)
print(vetorI)
print(vetorP)
