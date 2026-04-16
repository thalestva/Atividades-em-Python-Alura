#Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

#Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

def validar_cpf():
    """Converte o CPF para um formato sem pontos e traços, verifica se tem 11 dígitos e se contém apenas números.
    Sem argumentos, o programa solicitará ao usuário que insira um CPF. O programa então processará a entrada e verificará se ela é válida de acordo com as regras estabelecidas.
    Retorna True se o CPF for válido, ou False caso contrário.
    """

    cpf = input("Digite seu CPF: ")
    
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
        return False
    
    if not cpf.isdigit():
        print("Erro: O CPF deve conter apenas números.")
        return False
    
    return True

if validar_cpf():
    print("CPF válido.")
