from random import randint
"""
Make a rock-paper-scissors game where it is the player vs the computer. The computer’s answer will be randomly generated, while the program will ask the user for their input. This project will better your understanding of while loops and if statements.
"""
posOutcomes = ("Tessoura", "Papel", "Pedra")

print("Números de partidas:")
numGames = int(input())

playerCount = 0
computerCount = 0


for x in range(numGames):
    x += 1

    print("PARTIDA NÚMERO: %s" % x)
    print()
    computerChoice = randint(0,2)
    print("Escolha uma opção:")
    print("%s = 0; %s = 1 ou %s = 2" % posOutcomes)
    playerChoice = int(input())

    if(posOutcomes[computerChoice] == posOutcomes[playerChoice]):
        print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
        print("Vocês empataram!")
    else:
        if(posOutcomes[computerChoice] == posOutcomes[0]):
            if(posOutcomes[playerChoice] == posOutcomes[1]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Computador ganhou!")
                computerCount += 1
            if(posOutcomes[playerChoice] == posOutcomes[2]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Jogador ganhou!")
                playerCount += 1
        
        if(posOutcomes[computerChoice] == posOutcomes[1]):
            if(posOutcomes[playerChoice] == posOutcomes[0]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Jogador ganhou!")
                playerCount += 1
            if(posOutcomes[playerChoice] == posOutcomes[2]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Computador ganhou!")
                computerCount += 1
        
        if(posOutcomes[computerChoice] == posOutcomes[2]):
            if(posOutcomes[playerChoice] == posOutcomes[0]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Computador ganhou!")
                computerCount += 1
            if(posOutcomes[playerChoice] == posOutcomes[1]):
                print("Computador: " + posOutcomes[computerChoice] + " V.S. Player: " + posOutcomes[playerChoice])
                print("O Player ganhou!")
                playerCount += 1
    print()

if(playerCount == computerCount):
    print("Player: %s V.S. Computer: %s" % (playerCount, computerCount))
    print("Vocês empataram!")
elif(playerCount > computerCount):
    print("Player: %s V.S. Computer: %s" % (playerCount, computerCount))
    print("O Player ganhou o game!")
else:
    print("Player: %s V.S. Computer: %s" % (playerCount, computerCount))
    print("O Computador ganhou o game!")