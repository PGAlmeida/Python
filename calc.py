import tkinter as tk

def calcula_imc():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get()) / 100
    genero = genero_var.get()

    if genero == 'Homem':
        imc = peso / (altura ** 2)
    else:
        imc = (peso * 0.9) / (altura ** 2)

    imc_resultado.config(text=f'Seu IMC é: {imc:.2f}')
    interpretacao = interpret_imc(imc)
    interpretacao_label.config(text=f'Você é considerado: {interpretacao}')

def interpret_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25.0 <= imc < 29.9:
        return "Acima do Peso"
    else:
        return "Obeso"
    
root = tk.Tk()
root.title("Calculadora de IMC")
peso_label = tk.Label(root, text="Peso (Kg): ")
peso_label.pack()
peso_entry = tk.Entry(root)
peso_entry.pack()

altura_label = tk.Label(root, text="ALtura (cm): ")
altura_label.pack()
altura_entry = tk.Entry(root)
altura_entry.pack()

genero_var = tk.StringVar()
genero_label = tk.Label(root, text="Seleciona o genero: ")
genero_label.pack()
homem_radio = tk.Radiobutton(root, text='Homem', variable=genero_var, value="Homem")
mulher_radio = tk.Radiobutton(root, text='Mulher', variable=genero_var, value="Mulher")
homem_radio.pack(anchor = 'w')
mulher_radio.pack(anchor = 'w')

botao_calculadora = tk.Button(root, text="Calculate imc", command=calcula_imc)
botao_calculadora.pack()

imc_resultado = tk.Label(root, text="")
imc_resultado.pack()
interpretacao_label = tk.Label(root, text="")
interpretacao_label.pack()

root.mainloop()