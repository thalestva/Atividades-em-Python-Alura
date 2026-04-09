#João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

#Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

#Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

def calcular_gorjeta():
    """Calcula a gorjeta com base no valor da conta e na porcentagem de gorjeta fornecida pelo usuário.
    Sem argumentos, o programa solicitará ao usuário que insira o valor da conta e a porcentagem de gorjeta. O programa então processará as entradas, calculará a gorjeta e o total a ser pago, e exibirá os resultados.
    Sem retorno, o programa apenas exibe os resultados na tela.
    """
    try:
        conta = float(input("Digite o valor da conta: R$ "))
        gorjeta = float(input("Digite a porcentagem da gorgeta: ")) / 100 * conta
        gorjeta = round(gorjeta, 2)
        total = conta + gorjeta
        total = round(total, 2)
        print("Valor da gorjeta: R$ " + str(gorjeta))
        print("Total a pagar: R$ " + str(total))
    except ValueError:
        print("Por favor, insira um valor válido para a conta.")

calcular_gorjeta()