import os 
caminho = input("Digite um caminho da biblioteca: ")
c = r"C:\Faculdade\ALgoritmo\Nova Pasta"
lista = os.listdir(caminho)
lista1 = os.listdir(c)
print(len(lista))
print(len(lista1))