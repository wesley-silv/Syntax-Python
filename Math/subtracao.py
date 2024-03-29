def subtracao():
  """Subitração calc function"""
  print("Calculando a subtração")
  print("Quantos valores deseja subtrair em: 1) Dois valores, 2) Três valores, 3) Quatro valores, 4) Cinco valores")
  valores = float(input("Quantidade de valores: "))
  if(valores == 1):
      print("Calculando dois valores")
      subtracao_first_value = float(input("Primeiro valor: "))
      subtracao_second_value = float(input("Segundo valor: "))
      subtracao = (subtracao_first_value - subtracao_second_value)
      answer = "A subtração é igual a: {}".format(subtracao)
      print(answer, '\n')
  elif(valores == 2):
      print("Calculando três valores")
      subtracao_first_value = float(input("Primeiro valor: "))
      subtracao_second_value = float(input("Segundo valor: "))
      subtracao_third_value = float(input("Terceiro valor: "))
      subtracao = (subtracao_first_value - subtracao_second_value - subtracao_third_value)
      answer = "A subtração é igual a: {}".format(subtracao)
      print(answer, '\n')
  elif(valores == 3):
      print("Calculando quatro valores")
      subtracao_first_value = float(input("Primeiro valor: "))
      subtracao_second_value = float(input("Segundo valor: "))
      subtracao_third_value = float(input("Terceiro valor: "))
      subtracao_four_value = float(input("Quarto valor: "))
      subtracao = (subtracao_first_value - subtracao_second_value - subtracao_third_value - subtracao_four_value)
      answer = "A subtração é igual a: {}".format(subtracao)
      print(answer, '\n')
  elif(valores == 4):
      print("Calculando cinco valores")
      subtracao_first_value = float(input("Primeiro valor: "))
      subtracao_second_value = float(input("Segundo valor: "))
      subtracao_third_value = float(input("Terceiro valor: "))
      subtracao_four_value = float(input("Quarto valor: "))
      subtracao_five_value = float(input("Quinto valor: "))
      subtracao = (subtracao_first_value - subtracao_second_value - subtracao_third_value - subtracao_four_valsubtracao_five_value)
      answer = "A subtração é igual a: {}".format(subtracao)
      print(answer, '\n')
  else:
      print("Escolha a quantidade de valores da subtração")
                
subtracao()