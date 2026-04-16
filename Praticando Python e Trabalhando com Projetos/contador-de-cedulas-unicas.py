#Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.

#Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

### ------------------------- De acordo com o exercício devo conferir somente se o valor é inteiro e multiplo de 2 ------------------------------------------------------------

###Exemplo do exercício:
#Exemplo de Entrada:        Digite o valor do saque: 188
#Saída esperada:        Cédulas entregues:  1 de R$ 100  1 de R$ 50  1 de R$ 20  1 de R$ 10  1 de R$ 5  1 de R$ 2  
###Percebe-se que falta 1 real a ser entregue

### ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os


valor_a_sacar = 0
notas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}


def main():
    input_valor_valido()
    entrega_notas()
    exibir_notas()

def input_valor_valido():
    """Checa se o valor inserido é válido ou não e atribui o valor a variável valor_inicial e valor_a_sacar
    Sem args
    Sem retorno"""
    global valor_a_sacar
    while True:
        try:
            valor_a_sacar = int(input("Digite o valor do saque: "))
            if valor_a_sacar < 0:
                limpar_terminal()
                print("Erro: O valor deve ser positivo.")
            elif valor_a_sacar == 0:
                limpar_terminal()
                print("Erro: O valor a sacar não deve ser 0.")
            elif valor_a_sacar % 2 == 1:
                limpar_terminal()
                print("Erro: O valor deve ser múltiplo de 2.")
            else:
                limpar_terminal()
                break
        except ValueError:
            limpar_terminal()
            print("Erro: O valor deve ser um número inteiro")
    return


def entrega_notas():
    """Confere quais notas devem ser entregues e as entrega
    Sem args
    Sem retorno"""
    global valor_a_sacar
    for nota in [100, 50, 20, 10, 5, 2]:
        while valor_a_sacar >= nota:
            notas[nota] += 1
            valor_a_sacar -= nota


def limpar_terminal():
    """Limpa o terminal
    Sem args
    Sem retorno"""
    os.system('cls')


def exibir_notas():
    for nota in [100, 50, 20, 10, 5, 2]:
        print(f"{notas[nota]} de R$ {nota}")
    return


main()
