nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
escolha = input("Qual operação? aritmética ou ponderada (A/P) ").upper()

if escolha == "A":
    print("O resultado é:",((nota1+nota2)/2))

elif escolha == "P":
    peso1 = int(input("Digite o peso da primeira nota: "))
    peso2 = int(input("Digite o peso da segunda nota: "))
    print("O resultado é: {:.2f}".format(((nota1*peso1)+(nota2*peso2))/(peso1+peso2)))
