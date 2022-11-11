#---------------------------------------------------------------------
# Implemention of File Systems in Python
# Advance Software Paradigms - Quiz
# Shubham Jadhav
# To see cleaner code, please see MultiThreading.jl at my GitHub
# https://github.com/shubhjadhav/MS/tree/main/Fall%202022/CSCI_6221/Quiz
#---------------------------------------------------------------------

# Note: In some cases, if the code is copy pasted to an editor.
# You can see some wierd symbols/colors at indentations due to editor
# In that case, you can use the github link to access the same file to test the code
# Quiz/Object Oriented Design Patterns - There are 2 files, a python and a notebook
#   Either of those can be used to test the implementation
#
# To run the file: paste the code in https://www.online-python.com/

# QUESTION
#
# Let us suppose you are implementing file system. This file system contains folders and files. 
# A folder can contain other folders and files. Provide a very simple implementation using an OOP 
# for files and folders. 
# Folders and Files have just one common attribute: its name.
#
# Create a client object that can via methods:
#   print file/folder names
#   Add a file
#   Remove a file

# Class of folder, which can have an attribute name, and can have multiple files and folders
class Folder:
    
    # initializing constructor
    def __init__(self,name):
        self.name = name
        self.folders = []
        self.files = []

    # Method to add file to the folder
    def add_file(self, file):
        self.files.append(file)

    # Method to add folder to the folder
    def add_folder(self, folder):
        self.folders.append(folder)

    # Method to delete file from the folder
    def delete_file(self, file):
        self.files.remove(file)

    # Method to delete folder from the folder
    def delete_folder(self, folder):
        self.folders.remove(folder)

    # Method to print file names
    def print_file_names(self):
        for i,file in enumerate(self.files):
            print("File ",i+1,": ",file.name)
        if not self.files:
            print("No Files in ",self.name)

    # Method to print folder names
    def print_folder_names(self):
        for i,folder in enumerate(self.folders):
            print("Folder ",i+1,": ",folder.name)
        if not self.folders:
            print("No Folders in ",self.name)

# Class of file, which can have an attribute name
class File:
    
    def __init__(self, name):
        self.name = name


# Creating a folder and checking if it has files and folders (This will be our root folder)
current_semester = Folder("Fall 2022")
print(current_semester.name)
current_semester.print_file_names()
current_semester.print_folder_names()

# Creating a file and adding to root folder and checking if root folder has any files
misc_file = File("Miscelleneous")
current_semester.add_file(misc_file)
current_semester.print_file_names()

# Creating a folder and checking if it has files and folders
asp = Folder("ASP")
print(current_semester.name)
asp.print_folder_names()
asp.print_file_names()

# Creating dummy entries of file names
asp_chapters = [
    "Preliminaries", 
    "Evolution of the Major Programming Languages",
    "Describing Syntax and Semantics",
    "Lexical and Syntax Analysis",
    "Names, Bindings, and Scopes",
    "Data Types",
    "Expressions and Assignment Statements",
    "Statement-Level Control Structures",
    "Subprograms",
    "Implementing Subprograms",
    "Abstract Data Types and Encapsulation Constructs",
    "Support for Object-Oriented Programming"
]

# Creating files and adding them to ASP folder
for i,chapter in enumerate(asp_chapters):
    globals()[f'asp_chapter_{i}'] = File(chapter)
    asp.add_file(globals()[f'asp_chapter_{i}'])

# Checking if ASP Folder has files
asp.print_file_names()

# Checking if the instances are created correctly and ASP files are not appened to root folder
current_semester.print_file_names()

# Adding ASP folder to root folder and checking if it has files and folders
current_semester.add_folder(asp)
current_semester.print_file_names()
current_semester.print_folder_names()

# Deleting a file from root folders and checking if thas been deleted properly
current_semester.delete_file(misc_file)
current_semester.print_file_names()
current_semester.print_folder_names()

# Deleting ASP folder from root folders and checking if thas been deleted properly
current_semester.delete_folder(asp)
current_semester.print_folder_names()

# At maximum the root folder will have hierarchy as following
#
#   Fall 2022 (folder)
#       - Miscelleneous (file)
#       - ASP (folder)
#           - Preliminaries (file)
#           - Evolution of the Major Programming Languages (file)
#           - Describing Syntax and Semantics (file)
#           - Lexical and Syntax Analysis (file)
#           - Names, Bindings, and Scopes (file)
#           - Data Types (file)
#           - Expressions and Assignment Statements (file)
#           - Statement-Level Control Structures (file)
#           - Subprograms (file)
#           - Implementing Subprograms (file)
#           - Abstract Data Types and Encapsulation Constructs (file)
#           - Support for Object-Oriented Programming (file)