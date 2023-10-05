notas_declaradas = {
    "jose": 9,
    "Maria": 10,
    "Felipe": 7
}
c = 1

while c <= 10:

    nome_que_vai_entrar = input("Digite o nome do aluno >> ")
    nota = int(input("Digite  nota do aluno "))


    if nome_que_vai_entrar in notas_declaradas:
        print("Já existe o aluno ", nome_que_vai_entrar)
    else:
        # Adicionando o aluno ao dicionário
        notas_declaradas[nome_que_vai_entrar] = nota
        print(notas_declaradas)

    c += 1

for chave, value in notas_declaradas:
    print(f'{chave}:{value}')

# Crie um dicionário que represente um 
# dicionário de sinônimos. Em seguida, 
# peça ao usuário para digitar uma palavra e, 
# se a palavra estiver no dicionário, 
# mostre o seu sinônimo.

# Crie um dicionário que represente um dicionário de sinônimos.

sinonimos = {
    "bom": "excelente",
    "grande": "enorme",
    "feliz": "alegre",
    "triste": "cabisbaixo",
    "alto": "elevado",
    "baixo": "rebaixado"
}


def main():
    while True:
        palavra = input("Digite uma palavra: ")

        if palavra == "sair":
            break

        if palavra in sinonimos:
            print("O sinônimo de '{}' é '{}'".format(palavra, sinonimos[palavra]))
        else:
            print("A palavra '{}' não está no dicionário.".format(palavra))


if __name__ == "__main__":
    main()

    
    


dicionario = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5"
}


terceiro_indice = dicionario["c"]
print(terceiro_indice)


dicionario = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5"
}


terceiro_indice = dicionario["c"]
print(terceiro_indice)


















sinonimos = {
    "feliz": "radiante",
    "triste": "desolado",
    "grande": "colossal",
    "pequeno": "minúsculo",
    "rápido": "veloz"
}

while True:
    palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

    if palavra == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    
    encontrado = False
    
    # Busca nas chaves do dicionário
    for chave in sinonimos:
        if palavra == chave:
            print("Sinônimo de", palavra, "é", sinonimos[chave])
            encontrado = True
            break
    
    # Se não foi encontrado nas chaves, busca nos valores do dicionário
    if not encontrado:
        for chave, valor in sinonimos.items():
            if palavra == valor:
                print("A palavra", chave, "é um sinônimo de", palavra)
                encontrado = True
                break
    
    # Se não foi encontrado, permite ao usuário adicionar a palavra e o sinônimo
    if not encontrado:
        novo_sinonimo = input(f"A palavra '{palavra}' não foi encontrada. Digite o sinônimo da palavra: ").lower()
        sinonimos[palavra] = novo_sinonimo
        print(f"Palavra '{palavra}' e seu sinônimo '{novo_sinonimo}' foram adicionados ao dicionário.")


sinonimos = {
    "feliz": "radiante",
    "triste": "desolado",
    "grande": "colossal",
    "pequeno": "minúsculo",
    "rápido": "veloz"
}

while True:
    palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

    if palavra == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    
    encontrado = False
    
    # Busca nas chaves do dicionário
    for chave in sinonimos:
        if palavra == chave:
            print("Sinônimo de", palavra, "é", sinonimos[chave])
            encontrado = True
            break
    
    # Se não foi encontrado nas chaves, busca nos valores do dicionário
    if not encontrado:
        for chave, valor in sinonimos.items():
            if palavra == valor:
                print("A palavra", chave, "é um sinônimo de", palavra)
                encontrado = True
                break
    
    # Se não foi encontrado, permite ao usuário adicionar a palavra e o sinônimo
    if not encontrado:
        novo_sinonimo = input(f"A palavra '{palavra}' não foi encontrada. Digite o sinônimo da palavra: ").lower()
        sinonimos[palavra] = novo_sinonimo
        print(f"Palavra '{palavra}' e seu sinônimo '{novo_sinonimo}' foram adicionados ao dicionário.")




sinonimos = {
    "feliz": "radiante",
    "triste": "desolado",
    "grande": "colossal",
    "pequeno": "minúsculo",
    "rápido": "veloz"
}

while True:
    palavra = input("Digite uma palavra para encontrar seu sinônimo (ou 'sair' para encerrar): ").lower()

    if palavra == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    
    if palavra in sinonimos:
        print("Sinônimo de", palavra, "é", sinonimos[palavra])
    else:
        print("Palavra não encontrada no dicionário de sinônimos.")
    if palavra not in sinonimos: 
        sinonimos[entrada_usuario, entrada_user_adj]
        print("Digite aqui uma nova palavra e seu respectivo sinonimo: ")
        entrada_usuario = input("Digite a palavra desejada: ")
        entrada_user_adj = input("Digite o sinonimo da palavra digitada anteriomente: ")

















dicionario = {'key': 'value', 'key2': 'value2'}
menino = {"nome": "Felicio", "idade": 18, "endereco": "Rua: Vinte e três"}

v = menino["nome"]
z = menino["idade"]
x = menino["endereco"]
print(v)
print(z)
print(x)

del menino["endereco"]
print(menino)

menino["notas"] = 7
print(menino)

if "nome" in menino:
    print("O nome do menino é:", menino["nome"])

