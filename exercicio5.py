while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    if len(senha) >= 8:
        print("perfeito")
    else:
        print("erro")
        break
    if senha == nome:
        print("Não pode colocar o nome")
        break
    else:
        print("perfeito")

    if  " " in senha:
        print("Não pode conter espaço")
        break
    else:
        print("Senha válida!")
    