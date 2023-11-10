'''
def fun(x, y):
    if x > y:
        print('O menor é ', y)
    elif x < y:
        print('O menor é: ', x)
    else:
        print('Os dois são iguais')

x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
fun(x, y)


def fun(n):
    vet = []
    soma = 0
    for i in range(n):
        vet.append(int(input('Informe um numero: ')))
        soma+=vet[i]
    return soma


n = int(input('entre com a quantidade: '))
soma = fun(n)
print('A soma dos numeros do vetor é %d' %soma)
'''
'''
def maior(vet, n):
    maior = vet[0]
    for i in range(n):
        if vet[i] > maior:
            maior = vet[i]
    return maior

def menor(vet, n):
    menor = vet[0]
    for i in range(n):
        if vet[i] < menor:
            menor = vet[i]
    return menor

vet = []
n = int(input('entre com a quantidade: '))
for i in range(n):
    vet.append(int(input('Informe um numero: ')))
resultmaior = maior(vet, n)
resultmenor = menor(vet, n)
print('O maior numero do vetor é', resultmaior)
print('O menor numero do vetor é', resultmenor)
'''
'''
def par(vet, n):
    par=0
    cont=0
    for i in range(n):
        if i%2!=0:
            par += vet[i]
            cont+=1
    mediaPar = par/cont
    return mediaPar



def impar(vet, n):
    imapr=0
    cont=0
    for i in range(n):
        if i%2==0:
            imapr += vet[i]
            cont+=1
    mediaPar = imapr/cont
    return mediaPar


vet = []
n = int(input('entre com a quantidade: '))
for i in range(n):
    vet.append(int(input('Informe um numero: ')))
mediaPar = par(vet, n)
mediaImpar = impar(vet, n)
print('A media dos numero par do vetor é', mediaPar)
print('A media dos numero impar do vetor é', mediaImpar)
'''
'''
def fat(x):
    atual=1
    while(atual <= x):
        fati = fati*atual
        atual = atual+1
    return fati

x = int(input('entre com um número: '))
fatorial = fat(x)
print("O fatorial de %d é igual a %d" %(x, fatorial))
'''
def media(idade, n):
    cont = 0
    for i in range(n):
        cont = idade + cont
    media = cont/n
    return media

def acima(idade):
    m = media()
    cont = 0
    if idade > m:
        cont = cont + 1
    return cont

def abaixo(idade, nome, n):
    m = media()
    vet = []
    if idade < m:
        for i in range(n):
            vet[i] = nome[i]
    return vet[i]

nome = []
idade = []
n = 2
for i in range(n):
    nome.append(input('Informe o nome: '))
    idade.append(int(input('Informe a idade: ')))

    

media1 = media(idade, n)
acima1 = acima(idade)
abaixo1 = abaixo(idade, nome, n)

print(media1, acima1, abaixo1)