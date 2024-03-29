# This code is resposiblle for generate a calculator for some
def soma():
    print("Calculando a soma dos valores")
    options = {2: "Dois", 3: "Três", 4: "Quatro", 5: "Cinco"}
    print("Quantos valores deseja somar? Escolha entre 2 e 5.")
    quantity = int(input("quantity de valores: "))

    if quantity not in options:
        print("Por favor, selecione um número válido de valores.")
        return

    print(f"Somando {options[quantity]} valores")
    values = []

    for i in range(quantity):
        value = float(input(f"Digite o {i+1}º value: "))
        values.append(value)

    soma_total = sum(values)
    print(f"A soma dos valores é: {soma_total}")

soma()

