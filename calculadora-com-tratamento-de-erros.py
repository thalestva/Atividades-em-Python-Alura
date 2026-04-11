#Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.

#Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

#Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def calculadora():
    """Calcula com base nos valores que o usuario inserir, pede os valores e realiza as operações.
    Sem argumentos.
    Sem retorno.
    """
    operadores = ['+', '-', '*', '/']
    resultado = 0
    operação_escolhida = '/'
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
        return
    try:
        operacao_escolhida = input("Escolha a operação (+, -, *, /): ")
        if operacao_escolhida in operadores == False:
            raise ValueError
    except ValueError:
        print("Opção inválida")
        return
    try:
        segundo_numero = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
        return
    if operacao_escolhida == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao_escolhida == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao_escolhida == "*":
        resultado = primeiro_numero * segundo_numero
    else:
        try:
            resultado = primeiro_numero / segundo_numero
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            return
    try:
        casas_decimais = int(input("Insira quantas casas decimais deseja que o resultado tenha: "))
    except ValueError:
        print("Valor incorreto, favor inserir um número inteiro")
        return
    if casas_decimais == 0:
        resultado = round(resultado, 0)
    elif casas_decimais > 0:
        resultado = round(resultado, casas_decimais)
    print("Resultado: ", resultado)
calculadora()