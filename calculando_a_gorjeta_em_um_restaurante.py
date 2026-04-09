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