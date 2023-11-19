numero = int(input("Digite um número: "))

if numero > 100 and numero < 200:
    print("Numero {} dentro do intervalo entre 100 e 200".format(numero))
else:
    print("Numero {} fora do intervalo entre 100 e 200".format(numero))

numero = int(input("Digite um número: "))

if numero >= 100:
    if numero <= 200:
        print("O valor está no intervalo entre 100 e 200")
    else:
        print("O valor não esta no intervalo, o valor é maior do que 200")
else:
    print("O valor não esta no intervalo, o valor é menor do que 100")