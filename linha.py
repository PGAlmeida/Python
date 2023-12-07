nomes = ['Pedro', 'Rafael', 'Julio']
profissoes = ['Programador', 'Advogado', 'desempregado']

junta = {nome: profissao for nome, profissao in zip(nomes, profissoes)}

print(junta)


