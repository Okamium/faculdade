
def soma():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    
    resultado = num1 + num2

    print("-------------------------")
    print("Resultado da soma: ", resultado)

def subtracao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    resultado = num1 - num2

    print("-------------------------")
    print("Resultado da subtracao: ", resultado)

def multiplicacao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    resultado = num1 * num2

    print("-------------------------")
    print("Resultado da multiplicacao: ", resultado)

def divisao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    resultado = num1 / num2

    print("-------------------------")
    print("Resultado da divisao: ", resultado)

switch = {
    1: soma,
    2: subtracao,
    3: multiplicacao,
    4: divisao
}

operacao = int(input("Escolha o tipo de operacao que voce deseja: \n[1 para Soma]\n[2 para Subtracao]\n[3 para multiplicacao] \n[4 para divisao] \nInsira sua opcao: "))

def switch_case(case):
    func = switch.get(case, lambda: print("Caso invalido"))
    func()

switch_case(operacao)
