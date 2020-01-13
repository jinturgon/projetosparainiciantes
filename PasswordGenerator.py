import random
from random import shuffle
import string

"""
Write a programme, which generates a random password for the user. Ask the user how long they want their password to be, and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.
"""

passLen, passLett, passNum, passChars, password = 0,0,0,0,''
password = []
numbers = []
letters = []
symbols = []
chars = '~`!@#$%^&*()_-+={[}]|\:;<,>.?/'

while True:
    passLen = int(input("Qual será o tamanho da senha desejada? (6-32)\n:"))
    if passLen in range(6,33):
        break
    print("Resposta invalida!")

while True:
    passLett = int(input("Quantas letras deve ter na senha? (0 - "+ str(passLen) +")\n:"))
    if passLett in range(0,passLen+1):
        break
    print("Resposta invalida!")

while True:
    if passLen-passLett == 0:
        break
    passNum = int(input("Quantos números deve ter na senha? (0 - "+ str(passLen-passLett) +")\n:"))
    if passNum in range(0,passLen-passLett+1):
        break
    print("Resposta invalida!")

while True:
    if passLen-passLett-passNum == 0:
        break
    passChars = int(input("Quer que a senha tenha simbolos? (Sim: 1, Não: 0)\nSobrou "+ str(passLen-passLett-passNum) +" caracteres. Ele serão substituidos por simbolos ou letras e números (Dependendo da resposta).\n:"))
    if passChars in [1,0]:
        break
    print("Resposta invalida!")


if passLett != 0:
    for i in range(passLett):
        letters.append(random.choice(string.ascii_letters))
    print("Letras: ", end='');print(letters)

if passNum != 0:
    for i in range(passNum):
        numbers.append(random.choice(string.digits))
    print("Números: ", end='');print(numbers)

if passChars != 0:
    for i in range(passLen-passLett-passNum):
        symbols.append(random.choice(chars))
    print("Simbolos: ", end='');print(symbols)
else:
    for i in range(passLen-passLett-passNum):
        symbols.append(random.choice(string.ascii_letters+string.digits))
    print("Resto: ", end='');print(symbols)

password = numbers + letters + symbols

shuffle(password)
password = ''.join(map(str, password))
    
    


print("Sua senha é:\n:" + password)