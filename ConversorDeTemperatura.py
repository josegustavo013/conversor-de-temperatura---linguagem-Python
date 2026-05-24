def conversor_de_temperatura():
    print("bem vindo ao conversor de temperatura!")

    try:
        valor = float(input("digite um valor de temperatura: "))
        unidade = str(input("digite uma unidade: C(celsius),(Fahrenheit) ou K(kelvin): ")).upper()

        if unidade == "C":
            f = valor * 9/5 + 32
            k = valor + 273.15
            print(f"o valor em celsius é de: {valor}")
            print(f"o valor em Fahrenheit é igual a de: {f}")
            print(f"o valor em kelvin é de: {k}")


        elif unidade == "F":
            c = (valor - 32) * 5 / 9
            k = valor + 273.15
            print(f"o valor em Fahrenheit é de: {valor} ")
            print(f"o valor em kelvin é de: {k}")
            print(f"o valor em celsius é de: {c}")

        elif unidade == "K":
            c = (valor - 32) * 5 / 9
            f = valor * 9/5 + 32
            print(f"o valor em kelvin é de: {valor} ")
            print(f"o valor em Fahrenheit é de: {f}")
            print(f"o valor em celsius é de: {c}")

        else:
            print("ERRO! valor não encontrado!")

    except ValueError:
        print("erro! por favor digite apenas números para a temperatura!")

conversor_de_temperatura()