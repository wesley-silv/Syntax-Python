def aritimetic_media():
    """Media aritimetic function"""
    print("Calculando a média aritimética")
    print('Digite quatro valores para a realização da média aritimética.')
    fist_value = float(input("Digite o primeiro valor: "))
    secund_value = float(input("Digite o segundo valor: "))
    third_value = float(input("Digite o terceiro valor: "))
    four_value = float(input("Digite o quarto valor: "))
    media = (fist_value + secund_value + third_value + four_value) / 4
    answer = "A média aritimética dos valores é igual a: {}".format(media)
    return print(answer, "\n")


aritimetic_media()
