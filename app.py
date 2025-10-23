import os 

restaurantes = [{"nome":"praça", "categoria": "japonesa", "ativo": False},
                {"nome":"pizza suprema", "categoria": "italiana", "ativo": True},
                {"nome":"hamburgueria do zé", "categoria": "fast-food", "ativo": False}]

def exibir_nome_do_programa():
    print("\nSabor Express\n")

def voltar_ao_menu_principal():
    input("\nPressione Enter para continuar...")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print("\n")

def exibir_opcoes_do_menu():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Alternar estado do restaurante")
    print("4 - Sair da aplicação\n")

def finalizar_app():
    exibir_subtitulo("Finalizando aplicação...")

def opcao_invalida():
    print("Opção inválida! Tente novamente.\n")
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo("alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do reataurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} Foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("o restaurante nao foi encontrado")

    voltar_ao_menu_principal()

def cadastrar_restaurante():

    """
    
    Esta função cadastra novos restaurantes 
    
    Inputs:
    - Nome do Restaurante 
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    """

    exibir_subtitulo("cadastro de novos restaurantes!")
    nome_do_restaurante = input("Nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados: ")
    
    print(f"{"nome do restaurante".ljust(22)} | {"categoria".ljust(31)} | Status")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | categoria: {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def escolher_opcoes_do_menu():
    try:
        opcao_escolhida = int(input("escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes_do_menu()
    escolher_opcoes_do_menu()


if __name__ == "__main__":
    main()

