def terminal_command():
    command = input("Type a command for a definition: ") 
    if (command== "touch"):
        print("\n")
        print("This command is used to create files")
    if (command== "cd"):
        print("\n")
        print("This command will change the directory in order to execute other commands on a different directory")
    if (command== "ls"):
        print("\n")
        print("This command will show you the contents of the directory")
    if (command== "mkdir"):
        print("\n")
        print("This command will allow you to create a folder")
    if (command== "cat"):
        print("\n")
        print("Used to display text files")
terminal_command()
    
