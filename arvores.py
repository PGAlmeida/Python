def diamante(tamanho):
    for i in range(1, tamanho + 1):
        print(" " * (tamanho-i) + "*" * (2*i-1))
    for i in range(tamanho-1, 0, -1):
        print(" " * (tamanho-i) + "*" * (2*i-1))

def quadro(tamanho):
    for i in range(tamanho):
        if i == 0 or i == tamanho-1:
            print("*" * tamanho)
        else:
            print("*" + " " * (tamanho-2) + "*")

def triangulo(tamanho):
    for i in range(tamanho, 0, -1):
        print("*"*i)

def tri(tamanho):
    for i in range(1, tamanho+1, 1):
        print("*"*i)

tam = int(input("Digite o tamanho: "))
print('-------------------------------------------------')
diamante(tam)
print('-------------------------------------------------')
quadro(tam)
print('-------------------------------------------------')
triangulo(tam)
print('-------------------------------------------------')
tri(tam)