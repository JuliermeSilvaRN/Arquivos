nome = input("Qual seu nome: ")
altura = float(input("Qual sua altura: "))
peso = float(input("Qual seu peso: "))

icm = peso / (altura**2)

print("{} seu ICM = {} ".format(nome,icm))