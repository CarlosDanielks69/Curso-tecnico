lista = []

while True:
  
  print("[1] - Adicionar")
  print("[2] - Listar")
  print("[3] - Encerrar")

  opcao = input("Selecione: ")

  if opcao == "1":
    lista.append(input("Adicione; "))
    input("\n\nPressione qualquer tecla para continuar...")

  elif opcao == "2":

    for i in lista:
      print(f"- {i}")

    input("\n\nPrecione qualqu er tecla para continuar...")

  elif opcao == "3":
    print("Saindo...")
    break

  else:
    print("Opcao invalida!")
    input("\n\nPressione qualquer tecla para continuar...")
