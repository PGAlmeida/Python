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

segundo = int(input('Entre com a quantia de segundos: '))
converter(segundo)
