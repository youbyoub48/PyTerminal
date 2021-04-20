import os
boucle = True
while boucle:
    command = input("#")
    if command == "exit":
        boucle = False
    print(os.system(command))