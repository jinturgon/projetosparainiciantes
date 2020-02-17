from random import randint
"""
Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.
"""
numRandom = randint(0,1)

print("Insira um valor:")
numResposta = int(input())

if (numRandom == numResposta):
    print("Você acertou!")
elif (numRandom < numResposta):
    print("Você errou! O número randômico é menor que ")
    print(numResposta)
else:
    print ("Você errou! O número randômico é maior que ")
    print(numResposta)