import os
boucle = True
PATH = os.path.abspath(os.path.split(__file__)[0])
print(PATH)
while boucle:
    command = input("#")
    if command == "exit":
        boucle = False
    if command.count("cd") == 1:
        PATH = command.replace("cd ","")
    command = "cd "+PATH+"&&"+command
    a = os.system(command)
    a = str(a)
    print(a.replace("0",""))