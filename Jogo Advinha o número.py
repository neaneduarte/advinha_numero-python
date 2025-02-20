#Jogo Advinha o número
import random
print("=== JOGO DE ADIVINHAÇÃO ===")
numero_minimo = int(input("Qual o número mínimo do intervalo?\n"))
numero_maximo = int(input("Qual o número máximo do intervalo?\n"))
tentativas = int(input("Quantas tentativas para acertar?\n"))
numero_sorteado = random.randint(numero_minimo, numero_maximo)
while True:
  tentativa = int(input(f'Digite um número entre {numero_minimo} e {numero_maximo}: '))
  if tentativa == numero_sorteado:
    print('Parabéns você acertou o número.')
    break
  else:
    tentativas -= 1 #tentativas = tentativas - 1
    if tentativas == 0:
      print(f'Você não acertou o número e não tem mais tentativas. O número sorteado foi {numero_sorteado}')
      break
    else:
      print(f'Número errado. Tente novamente. Você ainda tem {tentativas} tentativas')