altura = float(input("Qual a sua altura? "))
peso = float(input("Qual seu peso? "))
sexo = input("Qual o seu sexo? M/F ").upper()

if sexo == "M":
    x = peso/(altura**2)

    if x < 11:
        print("Atleta")
    elif 11<=x<=13:
        print("bom")
    elif 14<=x<=20:
        print("normal")
    elif 21<=x<=23:
        print("elevado")
    elif x > 23:
        print("alto")

elif sexo == "F":
    x = peso / (altura ** 2)

    if x < 16:
        print("Atleta")
    elif 16<=x<=19:
        print("bom")
    elif 20<=x<=28:
        print("normal")
    elif 29<=x<=31:
        print("elevado")
    elif x > 31:
        print("alto")
