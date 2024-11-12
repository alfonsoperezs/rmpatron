from file_op import *

def process_command(command):
    args = command.split()
    num_args = len(args)
    if num_args < 2:
        print("Error: Arguments are missing")
        return
    match args[1]:
        case "-r":
            option_r(args[2], args[3:])
            