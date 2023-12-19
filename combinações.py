import itertools

roupas = ["Camisa", "Calça", "Vestido", "Bermuda"]
cores = ["Branco", "Preto", "Azul"]

combina = itertools.product(roupas, cores)

print(combina)