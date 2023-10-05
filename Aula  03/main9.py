# 5 -Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.
frase = "Olá, mundo!"

palavra = input("Digite uma palavra: ")

frase_concatenada = frase + " " + palavra

print(frase_concatenada)

#6 Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".*
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

mensagem = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

print(mensagem)

#7 Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.**
codigo_area = input("Digite o código de área: ")
numero = input("Digite o número principal: ")

numero_completo = f"+{codigo_area} {numero}"

print(numero_completo)

#8 Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.**
ingredientes = ["farinha", "ovos", "leite", "açúcar", "chocolate"]

frase_ingredientes = ", ".join(ingredientes)

print(frase_ingredientes)

#9 Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.**
adjetivo1 = input("Digite um adjetivo: ")
adjetivo2 = input("Digite outro adjetivo: ")
adjetivo3 = input("Digite mais um adjetivo: ")

frase = f"O céu é {adjetivo1}, {adjetivo2} e {adjetivo3}."

print(frase)
