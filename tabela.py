pessoas = {
    'id0001' : {'nome': 'Pedro', 'idade': 18, 'profissão': 'TI'},
    'id0002' : {'nome': 'Maria', 'idade': 65, 'profissão': 'Infermeira'},
    'id0003' : {'nome': 'Rafel', 'idade': 33, 'profissão': 'Advogado'}
}

for registro in pessoas.values():
    print(registro['nome'], registro['idade'], registro['profissão'])

print(f"{'Nome':^10} | {'Idade':^6} | {'Profissão':^12}")
print(f"{'-'*10} | {'-'*6} | {'-'*12}")

for registro in pessoas.values():
    print(f"{registro['nome']:<10} | {registro['idade']:^6} | {registro['profissão']:>12}")