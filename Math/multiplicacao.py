# def multiplicacao():
#     print("Calculando a multiplicação")
#     print("Quantos valores deseja multiplicar: 1) Dois valores, 2) Três valores, 3) Quatro valores, 4 Cinco valores")
#     value = float(input("Quantidade de valores: "))
#     if(value == 1):
#         multi_first_value = float(input("Primeiro valor: "))
#         multi_second_value = float(input("Segundo valor: "))
#         multiplication_result = (multi_first_value * multi_second_value)
#         answer = "A multiplicação dos valores é igual a: {}".format(multiplication_result)
#         print(answer, '\n')
#     elif(value == 2):
#         multi_first_value = float(input("Primeiro valor: "))
#         multi_second_value = float(input("Segundo valor: "))
#         multi_third_value = float(input("Terceiro valor: "))
#         multiplication_result = (multi_first_value * multi_second_value * multi_third_value)
#         answer = "A multiplicação dos valores é igual a: {}".format(multiplication_result)
#         print(answer, '\n')
#     elif(value == 3):
#         multi_first_value = float(input("Primeiro valor: "))
#         multi_second_value = float(input("Segundo valor: "))
#         multi_third_value = float(input("Terceiro valor: "))
#         mulit_four_value = float(input("Quarto valor: "))
#         multiplication_result = (multi_first_value * multi_second_value * multi_third_value * mulit_four_value)
#         answer = "A multiplicação dos valores é igual a: {}".format(multiplication_result)
#         print(answer, '\n')
#     elif(value == 4):
#         multi_first_value = float(input("Primeiro valor: "))
#         multi_second_value = float(input("Segundo valor: "))
#         multi_third_value = float(input("Terceiro valor: "))
#         mulit_four_value = float(input("Quarto valor: "))
#         multi_five_value = float(input("Quinto valor: "))
#         multiplication_result = (multi_first_value * multi_second_value * multi_third_value * mulit_four_value * multi_five_value)
#         answer = "A multiplicação dos valores é igual a: {}".format(multiplication_result)
#         print(answer, '\n')
#     else:
#         print("Escolha a quantidade de números a calcular!")
#         multiplicacao()
# multiplicacao()

def multiplicacao():
    print("Calculando a multiplicação")
    print("Quantos valores deseja multiplicar: 1) Dois valores, 2) Três valores, 3) Quatro valores, 4) Cinco valores")
    value = int(input("Quantidade de valores: "))
    
    if value < 1 or value > 5:
        print("Escolha uma quantidade válida de números para calcular!")
        multiplicacao()
        return
    
    valores = []
    for i in range(value):
        valor = float(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)

    multiplication_result = 1
    for val in valores:
        multiplication_result *= val
    
    answer = "A multiplicação dos valores é igual a: {}".format(multiplication_result)
    print(answer)

multiplicacao()
