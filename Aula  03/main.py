 #Defina as idades
idade1 = 45
idade2 = 18

# Compare as idades
if idade1 < idade2:
    print("A idade 1 é menor do que a idade 2.")
elif idade1 > idade2:
    print("A idade 1 é maior do que a idade 2.")
else:
    print("Ambas as idades são iguais.")

    # Solicite a idade do espectador
idade_espectador = int(input("Digite a idade do espectador: "))

# Verifique se o espectador é menor de idade
if idade_espectador < 18:
    print("Desculpe, este show é para maiores de 18 anos. Você não pode entrar.")
else:
    print("Bem-vindo ao show!")

# Solicite as três notas do aluno
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