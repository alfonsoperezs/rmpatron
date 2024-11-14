from command_reader import *

if __name__ == '__main__':
    run = True
    command_reader = Command_reader() 
    print("--------------------------- Welcome to RM PATRON ---------------------------")
    print("----------------------------------------------------------------------------")
    while run:
        command = input("-> ")
        run = command_reader.process_command(command)
        