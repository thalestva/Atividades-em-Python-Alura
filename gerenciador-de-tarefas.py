#Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

#Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

import os
i = 0
opcao_escolhida = 0
opcoes_possiveis = [1, 2, 3, 4]
tarefas = []

def main():
    opcao_escolhida = 0
    i = 0
    while True:
        while opcao_escolhida not in opcoes_possiveis:
            os.system('cls')
            menu()
            opcao_escolhida = input_opcao()
            i += 1
            if i > 0:
                print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
                os.system('cls')
        if opcao_escolhida == 1:
            opcao_escolhida = 0
            adicionar_tarefa()
        elif opcao_escolhida == 2:
            opcao_escolhida = 0
            listar_tarefas()
        elif opcao_escolhida == 3:
            opcao_escolhida = 0
            remover_tarefa()
        elif opcao_escolhida == 4:
            os.system('cls')
            print("Saindo do gerenciador de tarefas. Até mais!")
            break

def menu():
    """Exibe o menu no terminal
    Sem args
    Sem retorno"""
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

def input_opcao():
    """Pergunta ao usuário qual opção do menu ele quer selecionar
    Sem arg
    Sem retorno"""
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao not in opcoes_possiveis:
            raise ValueError
        else:
            return opcao
    except ValueError:
        print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")
        input("Digite Enter para seguir")
        return

def adicionar_tarefa():
    """Adiciona uma tarefa na lista de tarefas
    Sem args
    Sem retorno"""
    while True:
        tarefa_nova = input("Digite a tarefa: ")
        if tarefa_nova != "":
            tarefas.append(tarefa_nova)
            input("Tarefa adicionada! Digite Enter para prosseguir")
            return
        else:
            os.system('cls')
            print("Erro: Nenhum valor inserido")
            pass

def listar_tarefas():
    """Lista as tarefas da lista de tarefas
    Sem args
    Sem retorno"""
    os.system('cls')
    print("Tarefas:")
    i = 0
    if len(tarefas) > 0:
        for tarefa in tarefas:
            i += 1
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa")
    input("Enter para prosseguir")
    return

def remover_tarefa():
    """Remove uma tarefa de acordo com o index dela
    Sem args
    Sem retorno"""
    if len(tarefas) == 0:
        print("Erro: Nenhuma tarefa a remover")
        
    while True:
        os.system('cls')     
        listar_tarefas()
        try:    
            tarefa_remover = int(input("Digite o número da tarefa a ser removida"))
            if tarefa_remover > len(tarefas) or tarefa_remover < 1:
                print(f"Erro: Opção inválida! Escolha uma opção entre 1 e {len(tarefas)}.")
            else:
                break
        except ValueError:
            print("Erro: Entrada inválida! Digite um número.")
            input("Digite Enter para tentar novamente")
    
    del tarefas[tarefa_remover - 1]
    return
            

main()