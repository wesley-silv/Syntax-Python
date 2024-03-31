def cost_manager():
    print('\n          Management of cost in Python          '.upper())

    money = float(input(f'\nWhat the value received monthly: '))
    print(f'Received value RS                    {money:.2f}')
    dizy_month = float(money / 10)
    print(f'\nThe value of Dizy month is R$ {dizy_month:.2f}')
    money = (money - dizy_month)
    print(f'Rest value: R$                       {money:.2f}')
    
    print(f'\nWrite the items value to create the list:')
    # Dictionary with the content of items
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
    
    # Value of each item
    water = float(input(f'What the of                {costs_fixed[1]}: '))
    eletric_energy = float(input(f'What the value of {costs_fixed[2]}: '))
    internet = float(input(f'What the value of       {costs_fixed[3]}: '))
    phone = float(input(f'What the value of          {costs_fixed[4]}: '))
    graduation = float(input(f'What the value of     {costs_fixed[5]}: '))
    car = float(input(f'What the value of            {costs_fixed[6]}: '))
    rent = float(input(f'What the value of           {costs_fixed[7]}: '))
    gasoline = float(input(f'What the value of       {costs_fixed[8]}: '))

    # Calc the some and media of results
    total_cost = water + eletric_energy + internet + phone + graduation + car + rent + gasoline
    average_cost = total_cost / 8
    remove_values = money - total_cost
    
    # Print all results 
    print(f'\n          Total costs'.upper())
    print(f'{costs_fixed[1]}:          R${water:.2f}')
    print(f'{costs_fixed[2]}: R${eletric_energy:.2f}')
    print(f'{costs_fixed[3]}:       R${internet:.2f}')
    print(f'{costs_fixed[4]}:          R${phone:.2f}')
    print(f'{costs_fixed[5]}:     R${graduation:.2f}')
    print(f'{costs_fixed[6]}:            R${car:.2f}')
    print(f'{costs_fixed[7]}:           R${rent:.2f}')
    print(f'{costs_fixed[8]}:       R${gasoline:.2f}')

    print(f'\nTotal costs:                   R${total_cost:.2f}')
    print(f'Media of costs:                R${average_cost:.2f}')
    print(f'Reste value after of payment: R${remove_values:.2f}')

cost_manager()
