# COMO CRIAR LISTA USANDO TRUE, APPEND
lista = [1,3.28,-6,5,5, "Casa", 2.8, True]
lista.append(2)
print (lista)

#"REMOVE RETIRA O NUMERO QUE COLOCAR NA LISTA"

lista2 = [1,3,566,545,5678]
lista2.remove(1)
print(lista2)

del lista2[0]
print(lista2)

lista4 = len(lista)
print(lista4)

lista5 = [1,45,89,78,123,45,78,56]
for i in lista5:
    print(i)


(01) Crie uma lista chamada `numeros` que contenha os números inteiros de 1 a 5 e imprima-a na tela.
lista = [1,2,3,4,5,]
print (lista)

Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
lista = [1,2,3,4,5]
print (lista [2])

Exercício 3: Adicione o número 6 à lista numeros e imprima a lista atualizada.
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)

#Exercício 4: Remova o número 3 da lista numeros e imprima a lista resultante.
numeros = [1, 2, 3, 4, 5]
numeros.remove(3)
print(numeros)

Exercício 5: Crie uma lista chamada frutas contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
numeros = [1, 2, 3, 4, 5]
frutas = ["banana", "maçã", "uva"]
for i in frutas:
print(i)

Exercício 6: Use um loop for para percorrer e imprimir todos os elementos da lista frutas.
lista5 = ["banana", "maçã", "uva"]
for i in lista5:
    print(i)


numeros = [1, 2, 3, 4, 5]
if 5 in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")

