# # import os
# # print(os.path.abspath("f1&dj2knpXmU5rTMj#.txt"))
# import os

# def find(name, path):
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)

# def find_all(name, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             result.append(os.path.join(root, name))
#     return result

# import os, fnmatch
# def find(pattern, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         for name in files:
#             if fnmatch.fnmatch(name, pattern):
#                 result.append(os.path.join(root, name))
#     return result

# # find('*.txt', '/path/to/dir')

import os
import re
import win32api

def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                print (os.path.join(root, f))
                            
                break # if you want to find only one

def find_file_in_all_drivers(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        print(drive)
        find_file(drive, rex)

filename = input("Please enter file name you are looking for: ")
# find_file_in_all_drivers( 'test.txt' )
find_file_in_all_drivers( filename )
