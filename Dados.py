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

# Leitura e Escrita de Arquivos

# Leitura com 'r'  
arquivos = open("dados.txt", "r")
conteudo = arquivos.read()
print(conteudo)
arquivos.close()



# Escrita com'w'
arquivo = open("dados.txt", "w")
arquivo.write("Olá mundo !")
arquivo.close()


# Abertura e fechamento
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
