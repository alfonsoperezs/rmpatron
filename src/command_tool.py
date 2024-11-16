from file_op import *

class Command_tool:
    def __init__(self):
        self.__file_op = File_op()

    def process_command(self, command):
        args = command.split()
        num_args = len(args)
        if command == "exit":
            return False
        if num_args < 2:
            print("Error: Arguments are missing")
            return True
        else:
            self.__file_op.execute_operation(args[1], args[2:])
            return True
    
        
            
            