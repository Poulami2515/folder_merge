import os
import shutil
os.mkdir("C:/Users/Desktop/File operations (Python)/folder-merge-main/sub")
n=os.listdir("C:/Users/Desktop/File operations (Python)/folder-merge-main/f1")
m=os.listdir("C:/Users/Desktop/File operations (Python)/folder-merge-main/f2")
x=(len(n))
for i in range(x):
    new="C:/Users/Desktop/File operations (Python)/folder-merge-main/sub/file"+chr(i+65)
    os.mkdir(new)
    old1="C:/Users/Desktop/File operations (Python)/folder-merge-main/f1/"+n[i]
    new1="C:/Users/Desktop/File operations (Python)/folder-merge-main/sub/file"+chr(i+65)+'/'+n[i]
    shutil.move(old1, new1)
    old2="C:/Users/Desktop/File operations (Python)/folder-merge-main/f2/"+m[i]
    new2="C:/Users/Desktop/File operations (Python)/folder-merge-main/sub/file"+chr(i+65)+'/'+m[i]
    shutil.move(old2,new2)
    

