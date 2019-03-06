import os
import datetime

# print all methods/attributes
print (dir(os))

# print current directory
print (os.getcwd())

# change directory
os.chdir('C:/temp')
os.chdir('C:\\temp')

# list files
for f in os.listdir('C:/temp'):
    date_modified = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)
    print (f"{f} - {os.stat(f).st_size} - {date_modified}")

os.stat('C:/temp')[6]

# create dir
os.mkdir("some_folder")    
os.makedirs("C:/temp/some_folder")

# remove folders
os.rmdir("some_folder")
os.removedirs("C:/temp/some_folder")

# rename files/folder
os.rename("some_folder", "new_folder")


# transverse directories
for dirpath, dirnames, filesnames in os.walk('C:/temp/XML'):
    print (f"Directory path : {dirpath}")
    print (f"Directory name : {dirnames}")
    print (f"File name      : {filesnames}")

# environment variables
print (os.getenv("HOME"))
print (os.environ)

# avoiding directory delimeter guess
file_path = os.path.join(os.getenv("HOME"), 'new_file.txt')
print (file_path)


# getting only file name or directory name
file_path = 'C:/temp/sub1/sub2/sub3/test_file_path.txt'
print (os.path.basename(file_path))
print (os.path.dirname(file_path))
print (os.path.split(file_path))

# path exists
print (os.path.exists(file_path))

# isdir & isfile
file_name = "C:/temp/xml/sync.xml"
print (os.path.isdir(os.path.dirname(file_name)))
print (os.path.isfile(file_name))

# split extension
print (os.path.splitext(file_name))