'''
lista = [1, 2, 3]
print(lista)
lista = lista + [4]
print(lista)
lista = lista + [0, 0, 0]
print(lista)
lista[1] = lista[1] + lista[2]
print(lista)

'''
for n in range(0, 10, 1):
 print(n)

for n in range(10, 0, -2):
    print(n)

for n in range(10):
   print(n)

nomes = ['Pedro', 'Ana', 'Maria']
for n in nomes:
   print(n)

lista = [1, 3, 4, 7, 8]
for num in lista:
   if num>6:
      print(num)
