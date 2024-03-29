# Esse programa é destinado a fazer uso dos mais variados tipos de fórmulas matemáticas, para a realização de cálculos.
print("Escolha o tipo de operação matemática\n".upper())

def operations_matematics():
    """Operations_matimatics function"""
    print("Escolha o tipo do cálculo: A) Área do triângulo, B) Média aritimética, C) Soma, D) Subtração E) Multiplicação F) Tabuada\n")
    calc_type = input("Letra do Cálculo: ")
    if(calc_type == 'a'):
        import triangle_area
        triangle_area
        operations_matematics()
    elif(calc_type == 'b'):
        import media_aritimetic
        media_aritimetic
        operations_matematics()
    elif(calc_type == 'c'):
        import soma
        soma
        operations_matematics()
    elif(calc_type == 'd'):
        import subtracao
        subtracao
        operations_matematics()
    elif(calc_type == 'e'):
        import multiplicacao
        multiplicacao
        operations_matematics()
    elif(calc_type == 'f'):
        import tabuada
        tabuada
        operations_matematics()
    
operations_matematics()
# O programa está funcionado perfeitamente.
# Testado em 18/02/2023
# Todas as funcionalidades foram testadas.
