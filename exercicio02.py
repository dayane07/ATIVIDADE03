secreto = 20
resposta = int(input("digite o número secreto:"))

while resposta != secreto:
    if resposta > secreto:
        print("número muito alto! tente um menor.")
        resposta = int(input("tente novamente adivinhar o número secreto:"))
    elif resposta < secreto:
        print("número muito baixo! tente um maior. ")
        reposta = int(input("tente novamente adivinhar o número secreto:"))
        
    print("parabéns! você acertou o número secreto.")