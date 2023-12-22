from datetime import datetime

def calcular_tempo_passado(data):
    data_formatada = datetime.strptime(data, '%d/%m/%Y')
    tempo_passado = datetime.now() - data_formatada
    return tempo_passado




def converter(segundo):
    ano = segundo // (365.25 * 24 * 3600)
    resto_ano = segundo % (365.25 * 24 * 3600)
    mes = resto_ano // (30 * 24 * 3600)
    resto_mes = resto_ano % (30 * 24 * 3600)
    dia = resto_mes // (24 * 3600)
    resto_dia = resto_mes % (24 * 3600)
    hr = resto_dia // 3600
    resto_hr = resto_dia % 3600
    minuto = resto_hr // 60
    seg = resto_hr % 60
    print(f'{segundo} segundos é igual a {int(ano)} anos, {int(mes)} meses, {int(dia)} dias, {int(hr)}h:{int(minuto)}m:{int(seg)}s')


data_usuario = input("Digite uma data no formato DD/MM/AAAA: ")

try:
    tempo_passado = calcular_tempo_passado(data_usuario)
    converter(tempo_passado.total_seconds())
except ValueError:
    print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")