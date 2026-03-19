#-----------3.1 Vocabulary Review-------

#1. Git is a software tool with a command-line interface to save and send out repositories from a local computer, Github is a way to share git repositories onto an online/remote respoitory to share with others.
#2. Terminal is a text only window that displays commands sent out from the command line to the computer to run a shell. The command line is a type of interface that takes tect commands, including the terminal, but is where the user types out their commands to be read.
#3 A Local repository is a folder/group of files that can only be access from a single local computer, while a remote repository is a folder/group of files that is sent out to the web to be accessed from other computers as well.
#4. Version Control is a way to archive changes to a code over time, such as with git, and allows to see what exactly changed and when it happened.
#5. The staging area is the place within git where you can see what changes were made and allows you to choose changes to commit and review work before commiting. 
#6. git add adds all changes in the directory to be put into the staging area considered to be commited.
#7. git commit adds a version to be tracked in a project file and allows for a descriptive message to be added as well.
#8. git push sends commited files/directories from the local repository to a remote repository. 
#9. git status tracks which files are changed aand if they are commited or not, and displays untracked files that are not within Git.
#10. Git pull takes changes from a remote remository and adds them into a local repository.
#11.pwd prints the path of the current location within the computer files in terms of the parent and child directories. 
#12. ls lists out the files and folders in the current directory 
#13. cd changes the directory to a different directory
#14. nano creates or modifies a file within a directory.
#15. touch modifies and changes the timestamps of files/folders and can also be used to make new files.
#16. mv moves files or folders in linux
#17. rm deletes files or folders permanently
#18. cat is used to view, display and modify file contents within a terminal. 


#-------------3.2 A Directory Tree---------

#1. pwd
#2. ls
#3. cd ../briana_repo and git pull
#4. mv homework.py ../judy_decal homework.py
#5. cd ../judy_decal
#6. cat homework.py
#7. git add ., git commit, git push
#8. git pull .
    #this error means judy didn't pull the full/correct files from the remote repository into the local repository and therefore cannot save the changes to the remote one because it doesn't match.
#9. cd ../../recents


#-----------4.1 Data Types--------

def checkDataType(input):
    datatype = type(input)
    return datatype.__name__

print(checkDataType(5))

#-----------4.2 Data Types--------

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 3, 4, 5]
print(sumWithLoop(numbers))
#--------------6.1 Lists--------

def duplicateList(list):
    empty = []
    for item in list:
        for i in range(2):
            empty.append(item)
    return empty

print(duplicateList (["a", "b"]))
#---------6.2 Debugging------------

def square(num):
    return num * num

print(square(5))

list = ["hello", "world", ":)"]
print(duplicateList(list))