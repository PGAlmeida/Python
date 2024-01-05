def reverso(frase):
    return frase[::-1]

frase = input('Digite uma frase: ')
print(frase)
frase = reverso(frase)
print(f'A frase de tras para frente é: {frase}')