'''
conta = 0
x = 2
while(conta <= 5):
    print(x)
    conta += 1
else:
    print('Valor da variável conta é %d ' %conta)

'''

'''
soma = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        soma += n
else:
    print('A soma dos multiplos de tres é %d' %soma)

'''

'''
print('10:00')
for min in range(9, -1, -1):
    for seg in range(59, -1, -1):
        print('%02d:%02d' %(min, seg))
'''

'''
soma = 0
cont = 0
for num in range(0, 10, 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
else:
    print('A media é : %d' %(soma/cont))
'''

'''
soma = 0
cont = 0
num = int(input('Digite um número: '))
while(num != 0):
    if num % 2 == 0:
        soma += num
        cont += 1
    num = int(input('Digite um número: '))
else:
    if (cont == 0):
        print('Não existi notas validas')
    else:
        resul = soma/cont
        print('A media é : %d' %resul)
'''

'''
num = int(input('Digite um número: '))
sorte = int(input('Digite um número: '))
cont = 0
while(sorte != num):
    if sorte > num:
        print('Digite um numero menor')
        sorte = int(input('Digite um novo número: '))
    elif sorte < num:
        print('Digite um numero maior')
        sorte = int(input('Digite um novo número: '))
    cont += 1
else:
    print('Numero encontrado')
    print('quantidade de vezes jogadas: ' %cont)
'''   
