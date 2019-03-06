# not recommended way. You always must to close the file
file_name = 'C:/temp/XML/sync.xml'

f = open(file_name,'r')
print (f"File name : {f.name}")
print (f.readlines())
f.close()


# using context manager. File will be closed by the context manager
with open(file_name, 'r') as f:
    print (f"File name : {f.name}")
    print (f.readlines())
    
    # generator (read one line per interaction - large files  & memory optimization)
    # for line in f:
    #    print (line)

print (f"Is file closed ? - {f.closed}")

# writing files
file_name = 'C:/temp/XML/sample.txt'

with open(file_name, 'w') as f:
    f.writelines('line 1')
    f.writelines('line 2')
    f.writelines('line 3')



