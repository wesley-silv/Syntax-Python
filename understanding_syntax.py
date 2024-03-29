# Exploration of use with numbers

def expression():
  print('\nDeclarate your expression')
  expression = (48.5 * 4 + 200.45)
  print(str(f'Value of your expression: R${expression:.2f}\n'))
expression()

def division():
  print('Declaratin your expression of division')
  expression_one = (1250 / 4)
  expression_two = (1250 // 4)
  expression_three = (503 % 2)
  print(str(f'Value of: {expression_one}\nvalue of: {expression_two}\nvalue of: {expression_three}'))
division()

print(5 ** 5)