import os 

restaurantes = ["pizza", "churras", "hamburguer"]

def exibir_nome_do_programa():
    print("\nSabor Express\n")

def voltar_ao_menu_principal():
    input("\nPressione Enter para continuar...")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print("\n")

def exibir_opcoes_do_menu():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair da aplicação\n")

def finalizar_app():
    exibir_subtitulo("Finalizando aplicação...")

def opcao_invalida():
    print("Opção inválida! Tente novamente.\n")
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo("cadastro de novos restaurantes!")
    nome_do_restaurante = input("Nome do restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados: ")
    
    for restaurante in restaurantes:
        print(f"- {restaurante}")

    voltar_ao_menu_principal()

def escolher_opcoes_do_menu():
    try:
        opcao_escolhida = int(input("escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
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