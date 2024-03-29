print("Criando programas com python no conhecimento da linguagem, o mesmo deve ser usando para resolver problemas diversos.\n")

# Programa de login de usuários em um sistema.
def login():

  print("Login in the Web Page")
  users_cadastred = {'Wesley da Silva Conceicao' : 'wesleysilv23@gamil.com',
  'Meliny Sara de Paula Souza': 'melinysara6@gmail.com'}

  while():
    user_name = print(str(input("Digite o nome do usuário para ter acesso ao programa: ")))
    if(user_name in users_cadastred):
      print("Usuário cadastrado, acesso permitido")
    else:
      print("Usuário não cadastrado, acesso não permitido: ")

    # pensar em como resolver esse problema do programa, pois a verificação não esta encontrando os usuários cadastrados.
    # pesquisar na documentação do Python.

login()