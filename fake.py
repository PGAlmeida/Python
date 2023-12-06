from faker import Faker

gerador = Faker()
fa = Faker('pt-br')
for i in range(2):
    print(fa.name())
    print(gerador.address())
    print("#" * 5)