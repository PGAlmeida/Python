def crescente(vet):
    vetCrescente = sorted(vet)
    return vetCrescente

def decrescente(vet):
    vetDecrescente = sorted(vet, reverse=True)
    return vetDecrescente

vet = []
x = int(input('Digite o tamanho do vetor: '))
for i in range(x):
    vet.append(int(input('Digite um número: ')))
vetCrescente = crescente(vet)
vetDecrescente = decrescente(vet)
print(f'Vetor sem troca {vet}')
print(f'Vetor ordenado em forma crescente {vetCrescente}')
print(f'Vetor ordenado em forma decrescente {vetDecrescente}')
