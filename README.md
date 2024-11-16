# RMPATRON

`rmpatron` is a command-line application that allows you to search for and recursively delete files with a specific name starting from a given directory.
## How to run

> [!NOTE] 
> You need to have installed Python3 on your computer to use this tool.

Navigate to the `src` directory and use the following command:

```
python3 main.py
```

## Options
### Option -r

Find and delete all files with specific names in a directory and its subdirectories.

```
rmpatron -r [DIRECTORY] [name1, name2, ...]
```
## ToDo List
If you want to contribute to this proyect, there is something that we need to implement as soon as possible:
- [ ] Show information to the user during the execution.
- [ ] Reorganize the File_op class to improve code structure and facilitate its reuse in future projects.