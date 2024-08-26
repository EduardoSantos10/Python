#Estrutura de Dados

#Listas
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])
print(frutas[1])
print(frutas[2])

#Imprime Inverso
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

#Métodos de Lista

frutas = ["maçã", "banana", "laranja"]

#append
frutas.append("pera")
print(frutas)

#insert
frutas.insert(1, "uva")
print(frutas)

#remove
frutas.remove("banana")
print(frutas)

#pop
fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

#sort
frutas.sort()
print(frutas)

#reverse
frutas.reverse()
print(frutas)

#Lista de Compreensão
numeros = [2, 4, 6, 8, 10]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)