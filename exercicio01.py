número = int(input("digite um número inteiro:"))
impares = []

for contador in range(número, 0, -1):

    #código que se repete
  if  contador % 2 != 0:
    impares.append(contador)
    print(f"os números impares são: {impares}")
    
