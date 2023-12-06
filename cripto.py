from cryptography.fernet import Fernet

texto = input('digite uma frase ou palavra para criptografar: ')
print(f'texto original: {texto}')

chave = Fernet.generate_key()
fernet = Fernet(chave)
texto = fernet.encrypt(texto.encode())
print(f'texto criptografado: {texto}')

texto = fernet.decrypt(texto).decode()
print(f'texto decriptografado: {texto}')