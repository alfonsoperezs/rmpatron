import os
import shutil

class File_op:
    def __init__(self):
        self.__deleted = 0
        self.__deleted_path = []
    
    def execute_operation(self, option, args):
        self.__deleted = 0
        self.__deleted_path = []
        match option:
            case "-r":
                return self.__recursive_delete_by_name(args[0], args[1:])
            
    def __recursive_delete_by_name(self, path, names_files):
        content = os.listdir(path)
        for x in content:
            abs_path = os.path.join(path,x)
            if x in names_files:
                self.__remove_file_or_dir(abs_path)
            else:
                if os.path.isdir(abs_path):
                    self.__recursive_delete_by_name(abs_path,names_files)
        return self.__deleted, self.__deleted_path
                    
    def __remove_file_or_dir(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            self.__deleted += 1
            self.__deleted_path.append(path)
        else:
            os.remove(path)
            self.__deleted += 1
            self.__deleted_path.append(path)
        
    
            

            
            
            