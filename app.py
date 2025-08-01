import os

restaurantes = ["Pizza", "Sushi"]

def exibir_nome_do_programa():
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
  print("1. Cadastrar Restaurante")
  print("2. Listar Restaurantes")
  print("3. Ativar Restaurantes")
  print("4. Sair\n")
  
def finalizar_app():
  os.system("clear")
  print("Finalizando o app\n")
  
def opcao_invalida():
  print("Opção inválida!")
  voltar_ao_menu_principal()
  
def exibir_subtitulo(texto):
  os.system("clear")
  print(f"{texto}\n")

def voltar_ao_menu_principal():
  input("\nDigite uma tecla para voltar ao menu principal")
  main()
  
def cadastra_novo_restaurante():
  exibir_subtitulo("Cadastro de novos restaurantes")
  nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
  restaurantes.append(nome_restaurante)
  print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
  voltar_ao_menu_principal()

def listar_restaurantes():
  exibir_subtitulo("Lista de Restaurantes")
  for restaurante in restaurantes:
    print(f".{restaurante}")
  voltar_ao_menu_principal()

def escolher_opcoes():
  try:
    opcao_escolhida = int(input("Escolha uma opção: "))
    print(f"Você escolheu a opção {opcao_escolhida}")
    if (opcao_escolhida == 1):
      cadastra_novo_restaurante()
    elif(opcao_escolhida == 2):
      listar_restaurantes()
    elif(opcao_escolhida == 3):
      print("Ativar Restaurante")
    elif(opcao_escolhida == 4):
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system("clear")
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()
  
if __name__ == "__main__":
  main()
