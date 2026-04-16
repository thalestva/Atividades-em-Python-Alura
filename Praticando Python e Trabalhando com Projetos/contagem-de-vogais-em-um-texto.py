#Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

#Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém

def contar_vogais(texto):
    """Conta o número de vogais em um texto.
    Argumentos texto (str): O texto a ser analisado.
    Retorna int: O número de vogais no texto."""
    texto = texto.lower()  # Converte o texto para minúsculas para facilitar a contagem
    vogais = 'aeiouáéíóúâêîôûãõà'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
texto_usuario = input("Digite um texto: ")
print("O texto contém ", contar_vogais(texto_usuario), " vogais.")
