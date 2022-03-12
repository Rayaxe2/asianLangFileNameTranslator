!pip install googletrans
import os
from googletrans import Translator

translator = Translator()

forbiddenChars = "<>:\"/\\|?*"
print("A prefix will temporarly be prepended to file names used before renaming them. This prefix will be removed at the end of script. This is to prevent conflict during renaming")
prefix = input("Prefix: ")
while any(c in forbiddenChars for c in prefix) or prefix == "":
    print("The Prefix Contains One Of More Forbidden Characters {{ " + "<>:\"/\\|?*" + " }}")
    prefix = input("Please Select A Different Prefix: ")

path = input("File Path: ")
while "\\" not in path and ":\\Users" not in path and os.path.isdir(path):
    print("File Path Invalid")
    path = input("Please Select A Different File Path: ")
    
if path.split("\\")[-1] == "" or "." in path.split("\\")[-1]:
    path = path.rsplit("\\", 1)[0]

duplicatePaths = True
while duplicatePaths:
    duplicatePaths = False

    fullFilePaths = []
    fullFilePaths_trans = []
    fullFilePaths_trans_pre = []
    splitFilePaths_trans_pre = []
    
    for root, directories, files in os.walk(path):
        for file in files:
            fullFilePaths.append(os.path.join(root, file))
            fullFilePaths_trans.append(os.path.join(root, translator.translate(file)))
            fullFilePaths_trans_pre.append(os.path.join(root, (prefix +  translator.translate(file))))
            splitFilePaths_trans_pre.append([root, (prefix + translator.translate(file))])
        
    for splitPath_t_p in splitFilePaths_trans_pre:
        if fullFilePaths.count(os.path.join(splitPath_t_p[0], (prefix + splitPath_t_p[1]))) > 1  or
        fullFilePaths_trans.count(os.path.join(splitPath_t_p[0], (prefix + splitPath_t_p[1]))) > 1 or
        fullFilePaths_trans_pre.count(os.path.join(splitPath_t_p[0], (prefix + splitPath_t_p[1]))) > 1:
            print("The Chosen Prefix Causes Conflicts")
            prefix = input("Please Select A different Prefix: ")
            while any(c in forbiddenChars for c in prefix) or prefix == "":
                print("The Prefix Contains One Of More Forbidden Characters {{ " + "[No Text], <, >, :, \", /, \\, |, ?, *" + " }}")
                prefix = input("Please Select A Different Prefix: ")
            duplicatePaths = True
            break

for fullPath, splitPath_t_p in zip(fullFilePaths, splitFilePaths_trans_pre):
    fullPrefixedPath = os.path.join(splitPath_t_p[0], splitPath_t_p[1])
    os.rename(fullPath, fullPrefixedPath)
    print("Done Prefixing")