
 #excercio 01
 numero = int(input("Digite um número inteiro: "))
 if numero > 0:
     print("O número {} é positivo.".format(numero))
 elif numero < 0:
     print("O número {} é negativo.".format(numero))
 else:
     print("O número {} é zero.".format(numero))


 #excercio 02
 a = float(input("Digite o comprimento do lado a: "))
 b = float(input("Digite o comprimento do lado b: "))
 c = float(input("Digite o comprimento do lado c: "))

 if a == b == c:
     print("O triângulo é equilátero.")
 elif a == b or a == c or b == c:
     print("O triângulo é isósceles.")
 else:
     print("O triângulo é escaleno.") 

codigo_area = input("Digite o código de área: ")
numero = input("Digite o número principal: ")

numero_completo = f"+{codigo_area} {numero}"

print(numero_completo)
