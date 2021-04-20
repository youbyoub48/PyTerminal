import os
boucle = True
PATH = os.path.abspath(os.path.split(__file__)[0])
print("utiliser 'help' si vous avez besoin d'aide")
while boucle:
    command = input("#")
    b = True
    if command == "exit":
        boucle = False
    if command.count("cd") == 1:
        PATH = command.replace("cd ","")
    if command == "help":
        print("""
        Bienvenue dans le menu d'aide
        Vous pouvez utiliser toute les commande utilisable de votre terminal
        Utilisez la commande "exit" pour fermer le programme
        """)
        b = False
    if b:
        command = "cd "+PATH+"&&"+command
        a = os.system(command)
        a = str(a)
        print(a.replace("0",""))