#Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

#Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

#Pedra ganha de Tesoura (Pedra quebra Tesoura);
#Tesoura ganha de Papel (Tesoura corta Papel);
#Papel ganha de Pedra (Papel cobre Pedra);
#Se ambos escolherem a mesma opção, é um empate.

import random

def checar_vencedor(escolha_usuario, escolha_computador):
    """Determina o vencedor do jogo de pedra, papel e tesoura.
    Argumentos escolha_usuario (str): A escolha do usuário.
    Argumentos escolha_computador (str): A escolha do computador.
    Retorna str: O resultado da partida."""
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra"):
        return "Você venceu!"
    elif (escolha_usuario == "pedra" and escolha_computador == "papel") or \
         (escolha_usuario == "tesoura" and escolha_computador == "pedra") or \
         (escolha_usuario == "papel" and escolha_computador == "tesoura"):
        return "Computador venceu!"
opções = ["pedra", "papel", "tesoura"]

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
if escolha_usuario not in opções:
    raise ValueError("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
escolha_computador = random.choice(opções)
print("Computador escolheu: ", escolha_computador)
print(checar_vencedor(escolha_usuario, escolha_computador))