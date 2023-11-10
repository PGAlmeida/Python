'''
vet = []
n = int(input('entre com a quantidade: '))
for i in range(n):
    vet.append(int(input('Informe um numero: ')))

print('\n vetor')
for i in range(n):
    print(vet[i])

print("\n vetor")
print(vet)
#fyfhjbu


vet = []
n = int(input('entre com a quantidade: '))
soma = 0
for i in range(n):
    vet.append(int(input('Informe um numero: ')))
    soma+=vet[i]

print('\n vetor')
for i in range(n):
    print(vet[i])
print('soma igual a %d' %soma)
'''

vet = []
n = int(input('entre com a quantidade: '))
soma = 0
num=0
for i in range(n):
    vet.append(int(input('Informe um numero: ')))
    if vet[i]%2==0:
        soma+=vet[i]
        num+=1

media = soma/num

print('A média dos pares são: %0.2f' %media)