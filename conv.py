import tkinter as tk
from tkinter import filedialog as fd
from docx2pdf import convert

def convert_to_pdf():
    input_word_file = fd.askopenfilename(title="Selecionar o arquivo word", filetypes=[("Word Files", "*.docx")])
    if input_word_file:
        output_pdf_file = fd.asksaveasfilename(title="Salvar PDF", filetypes=[("PDF Files", "*.pdf")], defaultextension=".pdf")
        if output_pdf_file:
            convert(input_word_file, output_pdf_file)
            status_label.config(text="conversão concluida")

root = tk.Tk()
root.title("Converter Word em PDF")

convert_buttom = tk.Button(root, text="converter Word em PDF", command=convert_to_pdf)
convert_buttom.pack(pady=20)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()