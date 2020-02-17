fileIn = open()
fileOut = open()

for line in fileIn:
    if( '"F4"' in line ):
        fileOut.write(line)