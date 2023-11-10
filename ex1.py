
def tab(x):
    if x<1 and x>9:
        print('O numero é maior que 9 ou menor que 1')
    else:
        for i in range(11):
            print("%d * %d = %d" %(x, i, x*i))


def imc(peso, altura):
    calc = peso/(altura*altura)
    return calc


def fat(y):
    resultado=1
    count=1

    while count <= y:
        resultado *= count
        count += 1
    return resultado

print('1 - tabuada | 2 - IMC | 3 - fatorial')
num = int(input('Digite um número: '))

while num != -1:
    if num == 1:
        x = int(input('Digite um numero: '))
        tabu = tab(x)
    elif num == 2:
         peso = int(input('Digite seu peso: '))
         altura = int(input('Digite sua altura: '))
         resul = imc(peso, altura)
         print('o resultado é %0.2f' %(resul))
    else:
         y = int(input('Digite um numero: '))
         re = fat(y)
         print('O fatorial de %d é %d' %(y, re))
else:
    print('número invalido')
    print('1 - tabuada | 2 - IMC | 3 - fatorial')
    num = int(input('Digite um número: '))
print('O programa fechou!!!')

'''

def somatorio(n):
    soma = 0
    for n in range(1, n, -1):
        soma += n/(n*n)
    print(soma)


n = int(input('DIgite um número: '))
resultado = somatorio(n)
'''