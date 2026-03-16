import random

raio = 5
pi = 3.14159

area = print(pi*raio**2)

temp = 68

celciusTemp = print((temp - 32)*5/9)

livro = 25
caneta = 5

preço = print(livro*3 + caneta*2)

velocidade = 60
distancia = 150

tempo = print(distancia/velocidade)

nota1 = int(input("Quanto tirou no primeiro bimestre?"))
nota2 = int(input("Quanto tirou no segundo bimestre"))

notaFinal = (nota1+nota2)/2

print(f"Voce tirou {notaFinal}")

nota3 = int(input("Quanto tirou no primeiro?"))
nota4 = int(input("Quanto tirou no segundo"))

notaPonderada = (nota3*4+nota4*6)/10

print(notaPonderada)

compra1 = input("O que vai querer comprar?")
compra2 = input("E oque mais?")

compraQuant1 = int(input("Quantos vai querer comprar?"))
compraQuant2 = int(input("E quantos desse?"))

compra1Preco = random.randint(20, 30)*2
compra2Preco = random.randint(10, 20)*2

precoFinal = (compra1Preco*compraQuant1)+(compra2Preco*compraQuant2)
print(f"Comprou {compraQuant1} {compra1}, e {compraQuant2} {compra2}. O valor final sera de {precoFinal}.")

pagamento = int(input("Quanto ira pagar desse valor?"))
troco = pagamento - precoFinal

print(f"Ira ficar {troco} de troco.")