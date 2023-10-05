nome = "Kevin"
comprimento = len(nome)
print (comprimento)

x = "Guarulhos"
tipo = type(x)
print (tipo)

y = bool(input("Ditite algo, aqui dentro "))
z = type(y)
print (z)

int
n1 = "1"
x = int(n)
print (x,8)


float
n1 = "1.2"
x = float(n)
print (x+8)


str
n1 = 250
c = str(n1)
print(c,"JACINTO")

list
texto = "Python"
list = list(texto)
print (list)

tupla = (10,6,5,4)
tupla = (403,320,324)
print (tupla)


numeros = range(1,16)
for i in numeros:
    print(i)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

minimo = min(numeros)
maximo = max(numeros)

print("O número mínimo é", minimo, "o máximo é", maximo)
list1 = ["b", "d", "e","f"]
list2 = sorted*(list)
print(list)


RANGE FAZ UMA SEQUENCIA DE CONTAGEM
(2 INICIO, NUMERO DE PARTIDA, 20 NUMERO DE CHEGADA, 2 NUMERO DE CONTAGEM QUE DEVO PULAR)
EXERCICIOS (01)
numeros = range(2,22,2)
for i in numeros:
     print(i)



EXERCICIOS (02)
numeros = range(5,55,5)
for i in numeros:
     print(i)

Exercício 3: Escreva um programa que use a função type() para verificar o tipo de uma variável.
x = "Hello, world!"
tipo = type(x)
print(tipo)


Exercício 4: Escreva um programa que use a função print() para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.
nome = input("Qual é o seu nome? ")

print("Olá, {}! Seja bem-vindo(a) ao meu programa. Espero que voDcê se divirta.".format(nome))


Exercício 5: Escreva um programa que use a função range() para gerar os números ímpares de 1 a 10 e, em seguida, calcule e imprima a média desses números.

media = (1 + 3 + 5 + 7 + 9) / 5
print(f"A média dos números ímpares de 1 a 10 é {media:.2f}.")



Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
for i in range(2, 21, 2):
  print(i)

Exercício 2: Escreva um programa que imprima os números pares de 2 a 20.
for i in range(2, 21, 2):
  print(i)

Exercício 3: Escreva um programa que calcule a soma dos números de 1 a 100.

soma = sum(range(1, 101))
print(soma)

Exercício 4: Escreva um programa que imprima os múltiplos de 5 de 5 a 50.

numeros = range(5,55,5)
for i in numeros:
      print(i)

Exercício 5: Escreva um programa que peça ao usuário para digitar seu nome e imprima cada caractere do nome em uma linha separada.

nome = input("Digite seu nome: ")

for i in range(len(nome)):
  print(nome[i])








































# Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
# def main():
#   """
#   Imprime os números pares de 2 a 20.
#   """

#   for numero in range(2, 21, 2):
#     print(numero)


# if __name__ == "__main__":
#   main()


# Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 de 5 a 50 e, em seguida, calcule e imprima a soma desses múltiplos.
# def main():
#   """
#   Calcula e imprime a soma dos múltiplos de 5 de 5 a 50.
#   """

#   soma = 0
#   for numero in range(5, 51, 5):
#     soma += numero
#   print(soma)


# if __name__ == "__main__":
#   main()


