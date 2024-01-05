diario = {
    "Pedro": 10,
    "Rafael": 3,
    "João": 9,
    "Amanda": 7
}

print({nome: nota for nome, nota in diario.items() if nota > 7})