from file_op import *

def process_command(command):
    args = command.split()
    num_args = len(args)
    if num_args < 2:
        print("Error: Arguments are missing")
        return
    match args[2]:
        case "-r":
            remove_r(args[2:])
            