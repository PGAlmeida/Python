'''
n = int(input('entre com um número: '))
if n > 0:
    print('positivo')
elif n < 0:
    print('negativo')
else: 
    print('zero')

'''

'''
n1 = int(input('entre com um número: '))

if n1 % 2 == 0:
    print('par')
else:
    print('impar')

'''

'''
n1 = int(input('entre com um número: '))
n2 = int(input('entre com um número: '))

if n1 > n2:
    print(n1, 'e' , n2)
else:
    print(n2, 'e', n1)

'''

'''
a = int(input('entre com um número: '))
b = int(input('entre com um número: '))
c = int(input('entre com um número: '))


if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print('Triangulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Triangulo não existe')
'''

'''
alt = int(input('Digite seu peso: '))
sexo = input('Digite seu sexo: m-masculino e f-feminino')

if sexo == 'm':
    res = (72.7 * alt)-58
    print('Seu peso é ', res)
else:
    res = (62.1 * alt)-44.7

'''

'''
a = int(input('entre com um número: '))
b = int(input('entre com um número: '))
c = int(input('entre com um número: '))

if a>b and a>b:
    if b>c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b>a and b>c:
    if c>a:
        print(b, c, a)
    else:
        print(b, a, c)
else:
    if a>b:
        print(c, a, b)
    else:
        print(c, b, a)
'''

litro = int(input('quantos litros foram vendidos: '))
tipo = input('Digite a para álcool e g para gasolina: ')

if tipo == 'a':
    if litro <= 20:
        total = (2.10 * litro)*0.03
        res = (2.10 * litro)-total
        print('o valor a ser pago é: ', res)
    else:
        total = (2.10 * litro)*0.05
        res = (2.10 * litro)-total
        print('o valor a ser pago é: ', res)
else:
    if litro <= 20:
        total = (2.10 * litro)*0.04
        res = (2.10 * litro)-total
        print('o valor a ser pago é: ', res)
    else:
        total = (2.10 * litro)*0.06
        res = (2.10 * litro)-total
        print('o valor a ser pago é: ', res)