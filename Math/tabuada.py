def tabuada():
  print('Programa tabuada numérica'.upper(),'\n')
  table_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
  table = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
  value_multiply = float(input("Digite o número real ou inteiro para gerar a tabuada:")) # float deixa o número flutuante, assim é possível multiplicar inteiros por flutuantes.
  print('Menor número:',min(table_of_numbers),"Maior número:",max(table_of_numbers)," Quantidade de multiplicações:",len(table_of_numbers),'\n')
  answer = "\nResultado da tabuada numérica do número {}\n".format(value_multiply)
  for i in table: # i indica a posição dentro da lista table
    for index in table_of_numbers: # index indica uma posição dentro da lista table_of_numbers
      i = i + 1
      index = index * value_multiply
      print(f"{i} X {value_multiply} =".upper(), index)
      import time
      time.sleep(1)
    print(answer)
    break # impede que o primeiro for seja iniciado novamente, sendo usado apenas para instaciar os valores de i
  
  import matematics_operations
  matematics_operations()

tabuada() 
# tabuada criada com sucesso em 25/02/23
# Nesse programa os valores de uma lista foram usados como referência para a realização de uma multiplicação por um número inserido pelo usuário.
# Programa executado com sucesso em 28/02/2023, uma lista faz a interação do índice e a outra o número multiplicado.