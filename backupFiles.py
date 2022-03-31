import os
import shutil
import time

def backupFiles():
    path = input("Enter the path:- ")
    print(path)
    days = 30
    seconds = time.time() - (days*24*60*60)
    
    if os.path.exists(path):
        
        for rootFolders, folders, files in os.walk(path):

            if seconds >= deleting_files():
                removeFolder()

    else: 
        print("This path does not exists")

def deleting_files(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if not shutil.rmtree(path):
        print("Your folder has been removed")

    else:
        print("It's unable to detect the path")

backupFiles()
