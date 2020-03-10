import os
import re
import win32api

def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                path_url = str(os.path.join(root, f))
                path_array = path_url.split('\\')
                fileNameOnly = path_array[len(path_array) - 1]
                string_tmp = fileNameOnly+'|'+str(os.path.join(root, f).encode("utf-8")).replace('b','').replace('\'','')+'\n'
                print(fileNameOnly)
                # print (os.path.join(root, f))
                # ext = rex
                # text = os.path.join(root, f)
                # filenameonly = text[len(text)]

                with open("Output.txt", "a+") as path_url:
                    path_url.write("%s" % string_tmp)
                        # text_file = open("Output.txt", "w")
                        # text_file.write("result: %s" % os.path.join(root, f).encode("utf-8"))
                    path_url.close()            
                # break # if you want to find only one

def find_file_in_all_drivers(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        print(drive)
        find_file(drive, rex)

filename = input("Please enter file name you are looking for: ")
# find_file_in_all_drivers( '.txt' )
find_file_in_all_drivers( filename )
# import os
# for root, dirs, files in os.walk(\):
#     for file in files:
#         if file.endswith('.txt'):
#             print(file)