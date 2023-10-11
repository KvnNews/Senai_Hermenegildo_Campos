# cidade = 'São Carlos'
# endereco = 'Rua Cândido Padim, 25 - VIla Prado'
# completo = cidade + endereco
# print(cidade.startswith('Sâo'))
# print(cidade.endswith('Los'))
# print('Rua' in completo)
# print('Avenida' not in completo)

# Texto = "Python é uma linguagem legal"

# print(texto.count('é'))
# print(texto.find('Python',25,50))
# print(texto.rfind('é'))
# print(texto.index('é'))

# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.split('/'))

# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.splitlines())

# f = 'A força eletromotriz induzida em qualquer circuito fechado é igual ao negativo da variação do fluxo magnético com o tempo na área delimitada pelo circuito'
# f1 = f.replace('força','Bicicleta')
# f2 = f.replace('','#')
# print(f1)
# print(f2)

# a = '    Olá mundo    '
# print(f'{a}')
# b = a.strip()
# print(f'{b}')
# c = a.lstrip()
# print(f'{c}')
# d = a.rstrip()
# print(f'{d}')

#                                                                     # EXERCÍCIOS


# Exercício 1: Escreva um programa que verifique se a palavra "python" 
# está presente na string "Estou aprendendo Python".

# Receba a entrada do usuário
# frase = input("Digite uma frase: ")

# if "python" in frase.lower():
#     print("A palavra 'python' está presente na frase.")
# else:
#     print("A palavra 'python' não está presente na frase.")



# exercício 2: Escreva um programa que peça ao usuário para digitar 
# seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).

# nome = input("Digite seu nome: ")
# mensagem = "Seu nome começa com a letra 'A'." if nome[0].lower() == 'a' else "Seu nome não começa com a letra 'A'."
# print(mensagem)





# Exercício 3: Escreva um programa que peça ao usuário para digitar uma 
# senha e verifique se a senha contém pelo menos 8 caracteres.


# senha = input("Digite sua senha: ")


# if len(senha) >= 8:
#     print("Senha válida, contém pelo menos 8 caracteres.")
# else:
#     print("Senha inválida, não contém pelo menos 8 caracteres.")


# Exercício 4: Escreva um programa que peça ao usuário para digitar 
# um número e verifique se o número é uma representação numérica (não contém 
# letras ou símbolos).


# numero = input("Digite um número: ")


# if numero.isnumeric():
#     print("É uma representação numérica.")
# else:
#     print("Não é uma representação numérica.")



# frase = input("Digite uma frase: ")
# count = frase.lower().count('a')
# print(f"A letra 'a' aparece {count} vezes na frase.")

# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu
# comprimento. Informe também se as duas strings possuem o mesmo
# comprimento e são iguais ou diferentes no conteúdo.
# # Solicita que o usuário insira duas strings
# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")

# if string1 == string2:
#     print("As strings são iguais.")
# else:
#     print("As strings são diferentes.")

# 7

# Faça um programa que solicite o nome do usuário e imprima-o na vertical.
# e
nome = input("Digite seu nome: ")

for letra in nome:
    print(letra)
