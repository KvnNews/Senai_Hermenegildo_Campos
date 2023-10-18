# # Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.
# lista = [1, 2, 3, 4, 5]
# lista.pop(4)
# print(lista)

# # Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante
# lista = [10, 20, 30, 40, 50]
# lista.pop(1)
# print(lista)

#  Exercício 3: Crie uma pilha usando uma lista e implemente as operações  pop().

# Lista inicial
# lista = [1, 2, 3, 4, 5]

# # Adiciona um elemento à pilha usando append()
# lista.append(6)
# print("Elemento 6 adicionado à pilha.")

# # Remove e retorna o elemento do topo da pilha usando pop()
# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()
# print("Elemento", elemento_removido, "removido da pilha.")

# elemento_removido = lista.pop()  # Tentativa de remover de uma pilha vazia


# Exercício 4: Remova o primeiro elemento de uma lista e o último elemento usando pop() e imprima a lista resultante.
# def remove_lst(lista):
#     primeiro = lista.pop(0)
#     ultimo = lista.pop()
#     return lista


# lista = [1, 2, 3, 4, 5]

# lista_resultante = remove_lst(lista)

# print(lista_resultante)


# Exercício 5: Acesse os três primeiros caracteres de uma string.

# s = "Olá, mundo!"
# print(s[0])
# print(s[1])
# print(s[2])

# Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.

# def acs(lista):
#     return lista[1:-1]


# lista = [1, 2, 3, 4, 5]

# lista_resultante = acs(lista)

# print(lista_resultante)

# <**Desafio: Calculadora de Média >**

# Instruções:

# 1. Peça ao usuário que insira três notas (por exemplo, de 0 a 10).
# 2. Use a função **`input()`** para obter as notas como entrada do usuário e converta-as em números de ponto flutuante.
# 3. Calcule a média das três notas.
# 4. Com base na média, forneça uma avaliação:
#     - Se a média for maior ou igual a 7, imprima "Aprovado".
#     - Se a média for maior ou igual a 5 e menor do que 7, imprima "Recuperação".
#     - Se a média for menor do que 5, imprima "Reprovado".
# 5. Certifique-se de lidar com possíveis erros, como entradas inválidas (por exemplo, notas fora do intervalo de 0 a 10).

# def calculadora_media():

#     nota_1 = float(input("Digite a primeira nota: "))
#     nota_2 = float(input("Digite a segunda nota: "))
#     nota_3 = float(input("Digite a terceira nota: "))

    
#     while nota_1 < 0 or nota_1 > 10:
#         nota_1 = float(input("Digite a primeira nota: "))
#     while nota_2 < 0 or nota_2 > 10:
#         nota_2 = float(input("Digite a segunda nota: "))
#     while nota_3 < 0 or nota_3 > 10:
#         nota_3 = float(input("Digite a terceira nota: "))


#     media = (nota_1 + nota_2 + nota_3) / 3


#     if media >= 7:
#         print("Aprovado")
#     elif media >= 5:
#         print("Recuperação")
#     else:
#         print("Reprovado")


# if __name__ == "__main__":
#     calculadora_media()


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcule a média das notas
media = (nota1 + nota2 + nota3) / 3

# Verifique o desempenho do aluno com base na média
if media >= 7.0:
    print("O aluno está aprovado com média", media)
elif media >= 5.0:
    print("O aluno está em recuperação com média", media)
else:
    print("O aluno está reprovado com média", media)    