#File Type, Read, Write, close and different way of writing/reading file in python 

#  Binary vs Text Files in Python
'''
 Binary files include:
    Image files including .jpg, .png, .bmp, .gif, etc.
    Database files including .mdb, .frm, and .sqlite
    Documents including .doc, .xls, .pdf, and others.
'''
# Text file has no specific encoding and can be opened by a standard text editor
'''
 Every text file must adhere to a set of rules:
    Text files have to be readable as is. 
    They can (and often do) contain a lot of special encoding, especially in HTML or o
    ther markup languages, but you’ll still be able to tell what it says
    Data in a text file is organized by lines.
'''
# Opening a File in Python
# file_object = open(filename, mode)
# filename is the name of the file that you want to interact with(./workData.txt for current dir)
'''
The mode in the open function tells Python what you want to do with the file. 
There are multiple modes that you can specify when dealing with text files.
    'w' – Write Mode: This mode is used when the file needs to be altered and 
          information changed or added. Keep in mind that this erases the existing file to 
          create a new one. File pointer is placed at the beginning of the file.
          
    'r' – Read Mode: This mode is used when the information in the file is only
                     meant to be read and not changed inany way. 
                     File pointer is placed at the beginning of the file.
                     
    'a' – Append Mode: This mode adds information to the end of the file automatically. 
          File pointer is placed at the end of the file.
          
    'r+' – Read/Write Mode: This is used when you will be making changes to the file and reading 
           information from it. The file pointer is placed at the beginning of the file.
           
    'a+' – Append and Read Mode: A file is opened to allow data to be added to the end of the file 
           and lets your program read information as well. File pointer is placed at the end of the file.
'''
# When you are using binary files, you will use the same mode specifiers. 
# However, you add a b to the end. So a write mode specifier for a binary file is 'wb'. 
# The others are 'rb', 'ab', 'r+b', and 'a+b' respectively.

data_file = open("workData.txt", "r+")

# Closing a File in Python
data_file.close()

'''
In Python, the best practice for opening and closing files uses the with keyword. 
This keyword closes the file automatically after the nested code block completes:
'''
with open("workData.txt", "r+") as work_data:
    # File object is now open.
    # Do stuff with the file:
    print("This is the file name: ", work_data.name)
    # line = work_data.read()
    # print(line)
    
    line = work_data.read(6)
    print(line)
# File object is now closed.
# Do other things...

#Reading Data From a File in Python  fileobject.read(size) will read the entire file and print it out to the console 
# as either a string (in text mode) or as byte objects (in binary mode).

# Reading Text Files Line-by-Line With readline()
print("---------"*3)
with open("workData.txt", "r+") as workdata:
     print("This is the file name: ", workdata.name)
     #line_data = workdata.readline()
     # print(line_data)
     print(workdata.readlines())
     print("---------"*3)

# Processing an Entire Text File Line-By-Line 
with open("workData.txt", "r+") as work_data:
    for line in work_data:
        print(line)
        
with open("workData.txt", "a+") as work_datas:
    work_datas.write("\nThis data is on line 4\n")
print("---------"*3)

# Editing an Existing Text File with Python
# Open the file as read-only
with open("workData.txt", "r") as work_data:
    work_data_contents = work_data.readlines()

work_data_contents.insert(1, "This goes between line 1 and 2\n")

# Re-open in write-only format to overwrite old file
with open("workData.txt", "r+") as work_data:
    work_dataContents = "".join(work_data_contents)
    work_data.write(work_dataContents)

print("---------"*3)
with open("workData.txt", "r") as work_data:
    for line in work_data:
        print(line)
     
 


