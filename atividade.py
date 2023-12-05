
#Exercicio 1

def pagamento(valorPrestacao, atraso):
    if atraso > 0:
        multa = valorPrestacao * 0.03
        juros = valorPrestacao * (0.001 * atraso)
        pagar = valorPrestacao + multa + juros
        return pagar
    else:
       return valorPrestacao

totalPrestacao = 0
valorTotal = 0

while True:
    valorPrestacao = float(input('Entre com o valor da prestação (ou 0 para sair): '))
    if valorPrestacao == 0:
        break
    atraso = int(input('Entre com o número de dias em atraso: '))
    pagar = pagamento(valorPrestacao, atraso)
    print('Valor a ser pago: R$ %0.2f' %pagar)
    totalPrestacao += 1
    valorTotal += pagar

print('Relatório do dia: ')
print('Total de prestações pagas: %d' %totalPrestacao)
print('Valor total pago: R$ %0.2f' %valorTotal)


#exercicio 2

def calculaModa(vetorModa):
    if not vetorModa:
        return 'O Vetor está vazio, a Moda não pode ser calculada.'
    vetorModa.sort()
    moda = []
    frequenciaMax = 0
    numeroAtual = vetorModa[0]
    frequenciaAtual = 1
    
    for i in range(1, len(vetorModa)):
        if vetorModa[i] == numeroAtual:
            frequenciaAtual += 1
        else:
            if frequenciaAtual > frequenciaMax:
                moda = [numeroAtual]
                frequenciaMax = frequenciaAtual
            elif frequenciaAtual == frequenciaMax:
                moda.append(numeroAtual)
            numeroAtual = vetorModa[i]
            frequenciaAtual = 1
            
    if frequenciaAtual > frequenciaMax:
        moda = [numeroAtual]
    elif frequenciaAtual == frequenciaMax:
        moda.append(numeroAtual)
    if frequenciaMax == 1:
        return 'Não existe Moda neste Vetor.'
    else:
        return 'A Moda é: {}'.format(', '.join(map(str, moda)))

vetorModa = []
n = int(input('entre com a quantidade: '))
for i in range(n):
    vetorModa.append(int(input('Informe um numero: ')))
resultado = calculaModa(vetorModa)
print(resultado)


#exercicio 3

import random

def escolher():
    palavras = []
    with open('palavra_jogo.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    palavraEscolhida = random.choice(palavras)
    return palavraEscolhida

def mostrar(palavra, letraCorreta):
    palavraOculta = ''
    for letra in palavra:
        if letra in letraCorreta:
            palavraOculta += letra + ' '
        else:
            palavraOculta += '_ '
    return palavraOculta.strip()


palavra = escolher()
tentativaMaxima = random.randint(6, 11)
letraCorreta = set()
letraIncorreta = set()

print('Tente adivinhar a palavra oculta')

tentativas = 0

while tentativas < tentativaMaxima:
    letra = input('\nDigite uma letra: ').lower()
    
    if letra in letraCorreta or letra in letraIncorreta:
        print('Você já tentou esta letra. Tente novamente.')
        continue
    
    if letra in palavra:
        letraCorreta.add(letra)
    else:
        letraIncorreta.add(letra)
        tentativas += 1
    
    palavraOculta = mostrar(palavra, letraCorreta)
    print('Palavra: %s'  %palavraOculta)
    print('Letras corretas: ' + ', '.join(letraCorreta))
    print('Letras incorretas: ' + ', '.join(letraIncorreta))
    print('Tentativas restantes: %s' %(tentativaMaxima - tentativas))
    
    if set(palavra) == letraCorreta:
        print('Parabéns! Você adivinhou a palavra: %s'  %palavra)
        break

if set(palavra) != letraCorreta:
    print('Você perdeu! A palavra era: %s ' %palavra)


