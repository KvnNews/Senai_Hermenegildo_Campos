def calculadora():

    print("Selecione uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar igualdade")
    
    escolha = input("Digite o número da operação desejada: ")
    
    if escolha in ('1', '2', '3', '4', '5'):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        if escolha == '1':
            resultado = num1 + num2
        elif escolha == '2':
            resultado = num1 - num2
        elif escolha == '3':
            resultado = num1 * num2
        elif escolha == '4':
            if num2 == 0:
                resultado = "Erro: Divisão por zero"
            else:
                resultado = num1 / num2
        else:
            resultado = num1 == num2
        
        print(f"Resultado: {resultado}")
    else:
        print("Opção inválida")
calculadora ()
print("Selecione uma operação:")
calculadora()

# Crie duas telas no Figma.
# Coloque um botão na primeira tela.
# Selecione o botão e clique em Prototype.
# Clique em Add Interaction.
# Selecione On Click.
# Selecione a segunda tela na lista de telas.
# Clique em Create.


# Crie duas telas no Figma. Você pode fazer isso clicando em File > New e selecionando Frame.
# Coloque um botão na primeira tela. Você pode fazer isso clicando em Plugins > Basic Components > Button.
# Selecione o botão e clique em Prototype. Isso abrirá a janela de protótipo.
# Clique em Add Interaction. Isso abrirá o menu de interações.
# Selecione On Click. Isso significa que a interação será disparada quando o botão for clicado.
# Selecione a segunda tela na lista de telas. A lista de telas será exibida na parte inferior da janela de protótipo.
# Clique em Create. Isso criará a interação.


# desafio
# Criar um programa em python com esses dados
# Restaurante
# Precico de um cardapio
# Beber - Agua - refrigerante - vinho
# Comer - Macarronada - pizza -camarao
# mostrar as opções que  pessoa escolheu

import sys


# Declara as opções de bebidas
bebidas = ["Agua", "Refrigerante", "Vinho"]

# Declara as opções de comidas
comidas = ["Macarronada", "Pizza", "Camarão"]

# Imprime o menu
print("**Cardápio**")
print("Bebidas")
for bebida in bebidas:
    print(f"{bebidas.index(bebida) + 1} - {bebida}")
print("Comidas")
for comida in comidas:
    print(f"{comidas.index(comida) + 1} - {comida}")

# Recebe as opções do usuário
opcao_bebida = int(input("Selecione uma bebida: "))
opcao_comida = int(input("Selecione uma comida: "))

# Verifica se as opções são válidas
if opcao_bebida < 1 or opcao_bebida > len(bebidas):
    print("Opção de bebida inválida.")
    sys.exit()
if opcao_comida < 1 or opcao_comida > len(comidas):
    print("Opção de comida inválida.")
    sys.exit()
     
# Imprime as opções escolhidas
print("Opções escolhidas:")
print(f"Bebida: {bebidas[opcao_bebida - 1]}")
print(f"Comida: {comidas[opcao_comida - 1]}")



#desafio
# Criar um programa em python com esses dados
# Restaurante
# Precico de um cardapio
# Beber - Agua - refrigerante - vinho
# Comer - Macarronada - pizza -camarao
# mostrar as opções que  pessoa escolh


def subtrair(a, b):
    return a - b

def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    else:
        return a / b

def multiplicar(a, b):
    return a * b

def verificar_igualdade(a,b):
    return a == b

def divisao_int(a, b):
    return a // b 

def modulo(a, b):
    return a % b

def exponenciacao(a, b):
    return a ** b


def calculadora():
    print("Escolha a operação:")
    print("1. Subtração")
    print("2. Soma")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Verificar Igualdade")
    print("6. Divisão Inteira")
    print("7. Módulo")
    print("8. Exponenciação")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = subtrair(num1, num2)
        print(f"Resultado da subtração: {resultado}")
    elif escolha == '2':
        resultado = somar(num1, num2)
        print(f"Resultado da soma: {resultado}")
    elif escolha == '3':
        resultado = dividir(num1, num2)
        print(f"Resultado da divisão: {resultado}")
    elif escolha == '4':
        resultado = multiplicar(num1, num2)
        print(f"Resultado da multiplicação: {resultado}")
    elif escolha == '5':
        resultado = verificar_igualdade(num1, num2)
        print(f"Resultado da igualade: {resultado}")
    elif escolha == '6':
        resultado = divisao_int(num1, num2)
        print(f"Resultado da igualade: {resultado}")
    elif escolha == '7':
        resultado = modulo(num1, num2)
        print(f"Resultado da igualade: {resultado}")
    elif escolha == '8':
        resultado = exponenciacao(num1, num2)
        print(f"Resultado da igualade: {resultado}")
    else:
        print("Operação inválida!")

calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()
calculadora()

