import os
import shutil

def option_r(path, names_files):
    content = os.listdir(path)
    for x in content:
        abs_path = os.path.join(path,x)
        if x in names_files:
            remove_file(abs_path)
        else:
            if os.path.isdir(abs_path):
                option_r(abs_path,names_files)
            
            
def remove_file(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    
            

            
            
            