def combustivel_const():
    print("Calculando o gasto de combustível em uma viagem:\n".upper())
    value_gasoline = float(input('Qual o valor do litro da Gasolina: '))
    value_alcool = float(input('Qual o valor do litro do Alcool: '))
    veicle_eficiently = float(input('Gasto media do veículo:'))
    treweland = float(input('Distância da viagem em Km: '))

    if value_gasoline >= value_alcool: 
        calc = (treweland / veicle_eficiently) * value_gasoline
        print('O valor gasto na viagem com uso de gasolina é de:', abs(calc))
    else:
        calc = (treweland/ veicle_eficiently) * value_alcool
        print('O valor gasto na viagem com uso de alcool é de:', abs(calc))

combustivel_const()