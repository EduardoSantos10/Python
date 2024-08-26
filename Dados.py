# Entrada e Saida de Dados
nome = input("insira seu nome: ")
idade = input("insira sua idade: ")

print ("Olá, " + nome + "!" )
print("Você tem " + idade + " anos. ")


# Aplicando a função Int
idade = int(input("insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# Saida de Dados
nome = "Eduardo"
idade = 22
print(f"Olá, meu nome é {nome} e tenho {idade} anos. ")