IDADE_MINIMA = 18

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

altura = float(input("Digite sua altura: "))

contratar_servico = input("Deseja contratar o servico?: (Sim ou Nao): ").lower()

if(contratar_servico == "sim"):
    contratar_servico = True

elif(contratar_servico == "nao"):
    contratar_servico = False

else:
    print("Formato errado seu bosta")

print("---------------------------------")

print("Seu nome:", nome)

if(idade < IDADE_MINIMA): 
    print("Sua idade:", idade, " e voce e menor de idade")
else: 
    print("Sua idade:", idade, "anos e voce e maior de idade")

print("Sua altura:", altura)