import os
import shutil

class File_op:
    def __init__(self):
        self.__deleted = 0
        self.__deleted_path = []
    
    def ex_file_op(self, option, args):
        self.__deleted = 0
        self.__deleted_path = []
        match option:
            case "-r":
                return self.__option_r(args[0], args[1:])
            
    def __option_r(self, path, names_files):
        content = os.listdir(path)
        for x in content:
            abs_path = os.path.join(path,x)
            if x in names_files:
                self.__remove_file(abs_path)
            else:
                if os.path.isdir(abs_path):
                    self.__option_r(abs_path,names_files)
        return self.__deleted, self.__deleted_path
                    
    def __remove_file(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            self.__deleted += 1
            self.__deleted_path.append(path)
        else:
            os.remove(path)
            self.__deleted += 1
            self.__deleted_path.append(path)
        
    
            

            
            
            