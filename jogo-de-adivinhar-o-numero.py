#Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

#Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

#Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random

def jogar_adivinhacao():
    """Gera um número entre 1 e 100 aleatório e permite que o usuário tente adivinhar o número.
    Sem argumentos.
    Sem retorno."""
    numero_aleatorio = random.randint(1, 100)
    numero_escolhido = 0
    numero_maximo = 100
    numero_minimo = 1
    while numero_aleatorio != numero_escolhido:
        try:
            print("Tente adivinhar o número (", numero_minimo, "-", numero_maximo, ")")
            numero_escolhido = int(input())
            if numero_escolhido < 1 or numero_escolhido > 100:
                raise ValueError("fora_intervalo")
            if numero_escolhido == numero_aleatorio:
                print("Parabéns! Você acertou o número", numero_aleatorio, "!")
            elif numero_escolhido > numero_aleatorio:
                print("Muito alto! Tente novamente:", numero_escolhido, ".")
                numero_maximo = numero_escolhido-1
            elif numero_escolhido < numero_aleatorio:
                print("Muito baixo! Tente novamente:", numero_escolhido, ".")
                numero_minimo = numero_escolhido+1
        except ValueError as e:
            if str(e) == "fora_intervalo":
                print("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.")
            else:
                print("Entrada inválida: invalid literal for int() with base 10")

jogar_adivinhacao()