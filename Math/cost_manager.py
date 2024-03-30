# Generate for GPT chat
def cost_manager():
    print('Management of cost in Python')

    money = float(input(f'\nWhat the value received monthly: '))
    print(f'Received value RS {money:.2f}')
    dizy_month = float(money / 10)
    print(f'\nThe value of Dizy month is R$ {dizy_month:.2f}')
    money = (money - dizy_month)
    print(f'Rest value: R$ {money:.2f}')
    
    print(f'\nWrite the items value to create the list:')
    # Dicionário com os itens e seus respectivos nomes
    costs_fixed = {
        1: 'Water',
        2: 'Eletric energy',
        3: 'Internet',
        4: 'Phone',
        5: 'Graduation',
        6: 'Car',
        7: 'Rent',
        8: 'Gasoline'
    }
    
    # Pedindo os valores dos itens
    water = float(input(f'What the of Water{costs_fixed[1]}: '))
    eletric_energy = float(input(f'What the value of Eletric energy{costs_fixed[2]}: '))
    internet = float(input(f'What the value of Internet{costs_fixed[3]}: '))
    phone = float(input(f'What the value of Phone plan{costs_fixed[4]}: '))
    graduation = float(input(f'What the value of Graduation{costs_fixed[5]}: '))
    car = float(input(f'What the value of Car{costs_fixed[5]}: '))
    rent = float(input(f'What the value of Rent{costs_fixed[5]}: '))
    gasoline = float(input(f'What the value of Gasoline{costs_fixed[5]}: '))
  

    # Calculando a soma e a média dos valores
    total_cost = water + eletric_energy + internet + phone + graduation + car + rent + gasoline
    average_cost = total_cost / 8
    remove_values = money - total_cost
    
    # Imprimindo os resultados
    print(f'\nTotal costs')
    print(f'{costs_fixed[1]}: R${water:.2f}')
    print(f'{costs_fixed[2]}: R${eletric_energy:.2f}')
    print(f'{costs_fixed[3]}: R${internet:.2f}')
    print(f'{costs_fixed[4]}: R${phone:.2f}')
    print(f'{costs_fixed[5]}: R${graduation:.2f}')
    print(f'\nTotal costs: R${total_cost:.2f}')
    print(f'Media of costs: R${average_cost:.2f}')
    print(f'Reste value after of payment: R${remove_values:.2f}')

cost_manager()
