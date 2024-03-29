def soma():
  print("Calculando a soma dos valores")
  print("Quantos valores deseja somar: 1) Dois valores, 2) Três valores, 3) Quatro valores, 4) Cinco valores")
  valores = float(input("Quantidade de valores: "))
  if(valores == 1):
      print("Somando dois valores")
      some_first_value = float(input("Primeiro valor: "))
      some_second_value = float(input("Segundo valor: "))
      soma = some_first_value + some_second_value
      answer = "A soma dos valores é : {}".format(soma)
      return print(answer, "\n")
  elif(valores == 2):
      print("Somando três valores")
      some_first_value = float(input("Primeiro valor: "))
      some_second_value = float(input("Segundo valor: "))
      some_third_value = float(input("Terceiro valor:"))
      soma = some_first_value + some_second_value + some_third_value
      answer = "A soma dos valores é : {}".format(soma)
      return print(answer, "\n")
  elif(valores == 3):
      print("Somando quatro valores")
      some_first_value = float(input("Primeiro valor: "))
      some_second_value = float(input("Segundo valor: "))
      some_third_value = float(input("Terceiro valor:"))
      some_four_value = float(input("Quarto valor: "))
      soma = some_first_value + some_second_value + some_third_value + some_four_value
      answer = "A soma dos valores é : {}".format(soma)
      return print(answer, "\n")
  elif(valores == 4):
      print("Somando cinco valores")
      some_first_value = float(input("Primeiro valor: "))
      some_second_value = float(input("Segundo valor: "))
      some_third_value = float(input("Terceiro valor:"))
      some_four_value = float(input("Quarto valor: "))
      some_five_value = float(input("Quinto valor: "))
      soma = some_first_value + some_second_value + some_third_value + some_four_value + some_five_value
      answer = "A soma dos valores é : {}".format(soma)
      return print(answer, "\n")
  else:
      print("Selecione o valor referente ao cálculo desejado")
      
soma()