import os

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
  print("4. Sair")
  
def finalizar_app():
  os.system("clear")
  print("Finalizando o app\n")

def escolher_opcoes():
  opcao_escolhida = int(input("Escolha uma opção: "))
  print(f"Você escolheu a opção {opcao_escolhida}")
  if (opcao_escolhida == 1):
    print("Cadastrar Restaurante")
  elif(opcao_escolhida == 2):
    print("Cadastrar Restaurante")
  elif(opcao_escolhida == 3):
    print("Ativar Restaurante")
  else:
    finalizar_app()

def main():
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()
  
if __name__ == "__main__":
  main()
