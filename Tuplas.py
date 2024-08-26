#Criação e Acesso
ponto = (10, 20)

print(ponto[0])
print(ponto[1])

#Métodos de Tuplas
minha_tupla = (1, 2, 3, 2, 4, 2)

#count
print (minha_tupla.count(2))

#index
print (minha_tupla.index(2, 2))

#len
#print (minha_tupla.len(1, 2, 3, 2, 4, 2))


#Func com numeros var de argumentos
def soma_variavel(*numeros):
    total = 0
    for numero in numeros: 
        total += numero
    return total
print(soma_variavel(1, 2, 3))
print(soma_variavel(4, 5, 6, 7))

#Manejo de Exceções

#Try
try:
    #código que pode gerar uma exceção
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")


#Except
try:
    #código que pode gerar uma exceção
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: valor inválido")

#Finally
"""
try:
    #codigo que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    #realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close() # fechar o arquivo sempre, mesmo se ocorrer uma exceção
"""

#Exceções Personalizadas
def funcao():
    #codigo que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")
    
    try:
        funcao()
    except Exception as e:
        print(f"Erro: {str(e)}")
