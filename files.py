myfile = open("G:/My Drive/Internal Notes/GPC/Self-Study/Python/source_code/myfile.txt")

print ( myfile.read())
myfile.seek(0)

print ( myfile.readlines())

myfile.close()


with open('G:/My Drive/Internal Notes/GPC/Self-Study/Python/source_code/myfile.txt') as my_new_file:
    print (my_new_file.readlines())

with open ('G:/My Drive/Internal Notes/GPC/Self-Study/Python/source_code/new_myfile.txt', mode='w') as my_new_file:
    my_new_file.write("line 1\n")
    my_new_file.write("line 2\n")
    my_new_file.write("line 3\n")
