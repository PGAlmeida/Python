'''
def media(idades, n):
    cont = 0
    for i in range(n):
        cont += idades[i]
    media = cont / n
    return media

def acima(idades, n):
    m = media(idades, n)
    cont = 0
    for i in range(n):
        if idades[i] > m:
            cont += 1
    return cont

def abaixo(idades, nomes, n):
    m = media(idades, n)
    vet = []
    for i in range(n):
        if idades[i] < m:
            vet.append(nomes[i])
    return vet

def velhoNovo(idades, nomes, n):
    idadeMaisVelha = idades[0]
    idadeMaisNova = idades[0]
    nomeMaisVelha = nomes[0]
    nomeMaisNova = nomes[0]
    for i in range(n):
        if idades[i] > idadeMaisVelha:
            idadeMaisVelha = idades[i]
            nomeMaisVelha = nomes[i]
        if idades[i] < idadeMaisNova:
            idadeMaisNova = idades[i]
            nomeMaisNova = nomes[i]
    return nomeMaisNova, nomeMaisVelha

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado


nomes = []
idades = []
n = 30
for i in range(n):
    nome = (input('Informe o nomes: '))
    idade = int(input('Informe a idade: '))

    while idade < 0 or idade > 150:
        print("Idade inválida. Tente novamente.")
        idade = int(input(f"Informe a idade de {nomes[-1]}: "))

    nomes.append(nome)
    idades.append(idade)

media1 = media(idades, n)
acima1 = acima(idades, n)
abaixo1 = abaixo(idades, nomes, n)
nova, velha = velhoNovo(idades, nomes, n)

print('Média das idades: %0.2f' %media1)
print('Quantidade de pessoas acima da média: %d' %acima1)
print('Pessoas abaixo da média: %s' %abaixo1) 
print('Pessoa mais nova: %s' %nova)
print('Pessoa mais velha: %s' %velha)
for i in range(n):
    print('valor lido: %d | fatorial: %d' %(idades[i], fatorial(idades[i])))
    
'''
def maior(vet, x):
    maior = vet[0]
    for i in range(x):
        if vet[i] > maior:
            maior = vet[i]
    return maior

def segundoMaior(vet, x):
    m = maior(vet, x)
    seg = vet[0]
    for i in range(x):
        if vet[i] > seg and vet[i] != m:
            seg = vet[i]
    return seg

vet = []
x = int(input('Digite o tamanho do vetor: '))
for i in range(x):
    vet.append(int(input('Digite um número: ')))

maior1 = maior(vet, x)
segundo = segundoMaior(vet, x)
print('O maior é o número: %d' %maior1)
print('O segundo maior é o número: %d' %segundo)