import os
print(os.getcwd())  # get current working directory
print(os.getcwdb())  # get current working directory as bytes object
# change current working directory
os.chdir('C:\\Users\\luket\\OneDrive\\Desktop\\projects\\school\\python\\learningpython')
# list all files and directories in the current working directory
print(os.listdir())
# os.mkdir('newdir')  # create a new directory
os.rename('newdir', 'newdir2')  # rename a directory
os.rmdir('newdir2')  # remove a directory
# print(os.listdir())
