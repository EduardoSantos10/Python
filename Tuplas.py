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