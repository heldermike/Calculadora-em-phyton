def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def mutiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a/b 

while True :
  print("Selecione a operaçao desejada")

  print("+")
  print("-")
  print("*")
  print("/")
  print("Sair")

  opcao = input("Qual operacao você deseja fazer  ")

  if opcao == "Sair":
     print("Saindo... ")
     break

  num1 = float(input("Digite o primeiro numero   "))
  num2 = float (input("Digite o segundo numero   "))


  if opcao == '+':
    print("Resultado:", soma(num1, num2))
  elif opcao == '-':
    print("Resultado:", subtracao(num1, num2))
  elif opcao == '*':
    print("Resultado:", mutiplicacao(num1, num2))
  elif opcao == '/':
    print("Resultado:", divisao(num1, num2))
  else:
    print("Opção inválida")           
