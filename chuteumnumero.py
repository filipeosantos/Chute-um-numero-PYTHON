import random

x = random.randint(1,100)
tentativa = 0
numerouser = 0
print(x)



while numerouser != x:
    numerouser = int(input('Chute um numero entre 1 a 100: '))
    tentativa += 1


    if numerouser < x:
        print(f'Você errou! seu numero {numerouser} é menor que o numero misterioso ')

    elif numerouser > x:
        print(f'Você errou! seu numero {numerouser} é maior que o numero misterioso ')

    else:
        print(f'PARABÉNS VOCÊ ACERTOU! Você precisou de {tentativa} tentativas para acertar')















