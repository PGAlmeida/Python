import time

def cont(segundos):
    for i in range(segundos):
        min, seg = divmod(segundos - i, 60)
        texto = f"{min:02d}:{seg:02d}"
        print(texto, end="\r")
        time.sleep(1)
    print('Cronômetro zerado!!!!')

print("cronômetro")
x = int(input("digite o tempo (em segundos) para cronometrar: "))
cont(x)