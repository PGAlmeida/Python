palavras = []
with open("oi.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
print(palavras)