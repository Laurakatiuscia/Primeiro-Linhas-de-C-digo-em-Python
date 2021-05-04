#Criando uma calculadora

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

escolha = input("Selecione o número da operação desejada:\n 1- Soma \n 2- Subtração \n 3- Multiplicação\n 4- Divisão\n ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '1':
  print(num1, "+", num2, "=", add(num1, num2))
	
elif escolha == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))
	
elif escolha == '3':
  print(num1, "*", num2, "=", multiply(num1, num2))

elif escolha == '4':
	print(num1, "/", num2, "=", divide(num1, num2))

else:
	print("\nOpção Inválida!")