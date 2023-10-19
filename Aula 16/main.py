# # Imprime a data e hora atual no formato padrão
# print(datetime.datetime.now())

# # Imprime a data e hora atual no formato brasileiro
# print(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# # Imprime o ano atual
# print(datetime.datetime.now().year)

# # Imprime o mês atual
# print(datetime.datetime.now().month)

# # Imprime o dia atual
# print(datetime.datetime.now().day)

# # Imprime a hora atual
# print(datetime.datetime.now().hour)

# # Imprime o minuto atual
# print(datetime.datetime.now().minute)

# # Imprime o segundo atual
# print(datetime.datetime.now().second)

# # Imprime o microssegundo atual
# print(datetime.datetime.now().microsecond)


# import datetime
# data_atual = datetime.datetime.now()
# print(data_atual)


# import datetime
# from datetime import timedelta

# data_atual = datetime.datetime.now()
# data_futura = data_atual + timedelta(days=7)
# print(data_futura)


# import datetime



# date1 = datetime.date(2023, 9, 10)
# date2 = datetime.date(2023, 9, 20)
# diferenca = date2 - date1
# print(diferenca)


# #diretivas
# data_hora = datetime.datetime(2023, 9, 5, 15, 30, 0)
# data_hora_formatada = data_hora.strftime("%Y, %B, %A")
# print(data_hora_formatada)


# 1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.

# import datetime

# ano_nascimento = input("Digite seu ano de nascimento: ")

# ano_nascimento = int(ano_nascimento)

# data_atual = datetime.datetime.now()

# idade = data_atual.year - ano_nascimento

# print("Você tem {} anos.".format(idade))

# 2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.

# import datetime

# data_atual = datetime.datetime.now()

# data_futura = data_atual + datetime.timedelta(days=7)

# print("A data e hora daqui a 7 dias é:", data_futura)



# 3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.


# import datetime

# data_atual = datetime.datetime.now()

# print("O ano atual é:", data_atual.year)


# 4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).

import datetime

data_atual = datetime.datetime.now()

formato = "%d/%m/%Y %H:%M:%S"
data_hora_formatada = data_atual.strftime(formato)

print("A data e hora atuais são:", data_hora_formatada)