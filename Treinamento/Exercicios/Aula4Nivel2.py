nome = input("Qual seu nome: ")
n1 = float(input("Digite Nota1: "))
n2 = float(input("Digite Nota2: "))
n3 = float(input("Digite Nota3: "))

media = (n1 + n2 + n3) / 3
print(media)
if media >= 7:
    print("{} você foi Aprovado".format(nome))
else:
    if media >= 5.1 and media <= 6.9:
        print("{} você ficou Recuperação".format(nome))
    else:
        print("{} você foi Reprovado".format(nome))