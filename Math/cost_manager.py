# Generate for GPT chat
def cost_manager():
    print('Gerenciador de custos Python')

    money = float(input(f'\nQual o valor monetário mensal recebido: '))
    print(f'\nValor rebebido RS{money:.2f}')
    
    print(f'\nDigite os valores aos itens para gerar a lista:')
    # Dicionário com os itens e seus respectivos nomes
    items = {
        1: 'Water',
        2: 'Eletric energy',
        3: 'Internet',
        4: 'Phone',
        5: 'Graduation'
    }
    
    # Pedindo os valores dos itens
    water = float(input(f'Qual o valor da {items[1]}: '))
    eletric_energy = float(input(f'Qual o valor da {items[2]}: '))
    internet = float(input(f'Qual o valor da {items[3]}: '))
    phone = float(input(f'Qual o valor do plano de telefône {items[4]}: '))
    graduation = float(input(f'Qual o valor da mensalidade da faculdade {items[5]}: '))

    # Calculando a soma e a média dos valores
    total_cost = water + eletric_energy + internet + phone + graduation
    average_cost = total_cost / 5
    remove_values = money - total_cost
    
    # Imprimindo os resultados
    print(f'\nCustos totais:')
    print(f'{items[1]}: R${water:.2f}')
    print(f'{items[2]}: R${eletric_energy:.2f}')
    print(f'{items[3]}: R${internet:.2f}')
    print(f'{items[4]}: R${phone:.2f}')
    print(f'{items[5]}: R${graduation:.2f}')
    print(f'\nCusto total: R${total_cost:.2f}')
    print(f'Média dos custos: R${average_cost:.2f}')
    print(f'Valor restante após a realização dos pagamentos: R${remove_values:.2f}')

cost_manager()
