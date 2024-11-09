from command_reader import *

if __name__ == '__main__':
    print("--------------------------- Welcome to RM PATRON ---------------------------")
    print("----------------------------------------------------------------------------")
    while True:
        command = input("-> ")
        process_command(command)
        