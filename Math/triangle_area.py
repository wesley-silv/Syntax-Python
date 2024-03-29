def triangle_area():
  print("Calculando a área do triângulo")
  base = float(input("Digite o valor da base: "))
  altura = float(input("Digite o valor da altura: "))
  area = (base * altura) / 2
  answer = "A área do triângulo é de {} metros quadrados.".format(area)
  return print(answer,'\n')

triangle_area()