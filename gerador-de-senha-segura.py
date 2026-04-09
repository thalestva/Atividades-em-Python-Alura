#Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

#Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

import random

def gerar_senha_12_char():
    """Gera uma senha aleatória de 12 caracteres, contendo letras maiúsculas, minúsculas, números e caracteres especiais.
    Sem argumentos.
    Retorna str: A senha gerada."""
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    senha = ""
    for i in range(12):
        senha += random.choice(caracteres)
    return senha
senha_gerada = gerar_senha_12_char()
print("Senha gerada: ", senha_gerada)
