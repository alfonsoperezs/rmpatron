from command_tool import *

if __name__ == '__main__':
    run = True
    command_tool = Command_tool() 
    while run:
        command = input("[RMPATRON] -> ")
        run = command_tool.process_command(command)
        