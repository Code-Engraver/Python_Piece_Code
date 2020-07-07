# https://www.datacamp.com/community/tutorials/reading-writing-files-python
# In this file, based on the contents of the above link, 
# we will learn about deep exploration of the open function and how to handle the file in Python.

# Flat Files vs. Non-Flat Files
# It has a grand name, but it doesn't really mean much. 
# Flat Files is a file format that contains one record per line, 
# either plain text or a mixture of text and binary. 
# For example, suppose you store membership information. 
# The whole line is to store data corresponding to one person, 
# and each attribute is to display separately by a delimiter or separator. 
# Non-Flat Files is the opposite.

# How Python handles files
# When reading or writing files in Python, a file object called "handle" is required. 
# The function that returns this is the open function. 
# When you manage files, you may have text and binary files.
# For text files, there is an end-of-line delimiter (End-Of-Line, EOL), and \n is the default in Python. 
# In the case of binary files, there are no line delimiters because they consist of 0 and 1.

# Open function
# The parameters of the Open function are configured as follows. 
"""
    open(
    file, 
    mode='r', 
    buffering=-1, 
    encoding=None, 
    errors=None, 
    newline=None, 
    closefd=True, 
    opener=None
    )
"""
# The most important of these are the first and second parameters. 
# This file will cover the entire parameters, 
# but in fact, the most frequently used ones are the first and second parameters, 
# so please focus on them.

# ====================================================================================================

# file parameter
# The file parameter is an essential parameter in the open function. 
# Indicates the path where the file is located in the system, both relative and absolute paths are available.
import io
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_path(*args):
    return os.path.join(BASE_DIR, *args)
def result_delimiter():
    print(f"\n{'=' * 100}\n")

text_data_path = get_path('datasets', '005_text.txt')
print(f"file's path : {text_data_path}")

try:
    text_handle = open(text_data_path)
    print(f"text\n{text_handle.read()}")
except FileNotFoundError:
    print("No files found in path.")

result_delimiter()

# ====================================================================================================

# mode parameter
# The second parameter is the mode parameter. 
# This parameter defines how to access and determines whether the file is opened. 
# By default, it is set to "r" and various methods are arranged below.
"""
    r : Open file for reading only. Starts reading from beginning of file. This default mode.
    rb : Open a file for reading only in binary format. Starts reading from beginning of file.
    r+ : Open file for reading and writing. File pointer placed at beginning of the file.
    w : Open file for writing only. File pointer placed at beginning of the file. Overwrites existing file and creates a new one if it does not exists.
    wb : Same as w but opens in binary mode.
    w+ : Same as w but also allows to read from file.
    wb+ : Same as wb but also allows to read from file.
    a : Open a file for appending. Starts writing at the end of file. Creaters a new file if file does not exist.
    ab : Same as a but in binary format. Creates a new file if file does not exist.
    a+ : Same a a but also open for reading
    ab+ : Same a ab but also open for reading
"""

# ====================================================================================================

# read file
# Let me introduce the function of handle object. 

# For read(), introduce the entire text at once. 
# The number contained is the number of characters to print, 
# as will be the same in the readline() to be introduced later.
text_handle = open(text_data_path, "r")
print(text_handle.read())

result_delimiter()

text_handle = open(text_data_path, "r")
print(text_handle.read(2))

result_delimiter()

# Readline() takes a line by line. 
# Each time it is imported, the cursor waits in the next line. 
# If there is no next line, return None.
text_handle = open(text_data_path, "r")
print(">>>", text_handle.readline())
print(">>>", text_handle.readline())
print(">>>", text_handle.readline())
print(">>>", text_handle.readline())
print(">>>", text_handle.readline())
print(">>>", text_handle.readline())

result_delimiter()

# Because the handle itself is iterable, it can be used as follows. 
# It is important to note that it is recommended to close the handle after use through close().
text_handle = open(text_data_path, "r")
for line in text_handle:
    print(line)
text_handle.close()

result_delimiter()

# Readlines() return a list based on a line.
text_handle = open(text_data_path, "r")
print(text_handle.readlines())

# ====================================================================================================

# write file
# 'w' mode overwrites files. 
# It is not a form that is added every time it is executed, but it is written again. 
# The additional points are that the wrapping is manual 
# and that it is recommended to specify encoding.
write_text_file_path = get_path("datasets", "005_write_ex.txt")
write_text_handle = open(write_text_file_path, mode="w", encoding="utf-8")

write_text_handle.write("'w' mode overwrites files.\n")
write_text_handle.write("It is not a form that is added every time it is executed, but it is written again.\n")
write_text_handle.write("The line change is manual.\n")

write_text_handle.close()

# ====================================================================================================

# append file
# The 'a' mode will continue to write down the file. 
# You will see that lines are added every time you execute. 
# If the file does not exist, it also plays a new role.
sports = ["tennis, ", "soccer, ", "baseball\n"]
append_text_file_path = get_path("datasets", "005_append_ex.txt")
append_text_handle = open(append_text_file_path, mode="a", encoding="utf-8")
append_text_handle.writelines(sports)

append_text_handle.close()

# ====================================================================================================

result_delimiter()

# Seek Method
# Let's find out about see() and tell(). 
# seek() can change the cursor location of a file to any location. 
# The first parameter means the interval from the start point, 
# and the second parameter means the start point. 
# The default value for the second parameter is 0, which means the start of the file. 
# For other examples, 1 and 2 can come in, 
# each of which means the current cursor location, the end of the file. 
# or only 1 and 2 it is only possible in binary files. 
# tell() expresses the cursor position of the current file in bytes.
country_list = ['USA\n', 'Korea\n', 'China\n']
seek_method_handle = open(get_path("datasets", "005_seek_method_ex.txt"),mode="a+",encoding="utf-8")

for country in country_list:
    seek_method_handle.write(country)

print("The current handle's cursor position is:",seek_method_handle.tell())

seek_method_handle.seek(0)

print("The current handle's cursor position is:",seek_method_handle.tell())

for line in seek_method_handle:
    print(line)
seek_method_handle.close()

# ====================================================================================================

result_delimiter()

# next Method
# next() is simple. 
# Move the position of the read cursor to the next line.
next_method_handle = open(get_path("datasets", "005_text.txt"), "r")
for _ in range(5):
    print(next(next_method_handle))
next_method_handle.close()

# ====================================================================================================

result_delimiter()

# Ensure handle is closed and leverage with syntax
# Since only open() has been used so far, 
# it has always been necessary to close at the end of the code. 
# Of course, it's a code that ends in one line, 
# but in projects with a lot of I/O, even a single line becomes troublesome. 
# So it's with the phrase. 
# If you use with, close the handle automatically even if there is no code to close it.
file_handle1 = open(get_path("datasets", "005_text.txt"), "r")
print(f"Is closed? : {file_handle1.closed}")
file_handle1.close()
print(f"Is closed? : {file_handle1.closed}")

with open(get_path("datasets", "005_text.txt"), "r") as file_handle2:
    print(f"Is closed? : {file_handle2.closed}")
print(f"Is closed? : {file_handle2.closed}")

result_delimiter()

# ====================================================================================================

# So far, we have used the first and second parameters of open(). 
# Knowing this much of the open() will not have much trouble using it. 
# Before explaining the remaining parameters that are non-mainstream, 
# I will deal with json based on the practice.
json_dict = {
    "students" : [
        {
            "name" : "Dave",
            "age" : 24,
            "car" : {
                "brend" : "Audi",
                "type" : "SUV"
            }
        },
        {
            "name" : "Lee",
            "age" : 22,
            "car" : {
                "brend" : "BMW",
                "type" : "SUV"
            }
        }
    ]
}
json_file_path = get_path("datasets", "005_json_ex.json")
with open(json_file_path, "w") as f:
    json.dump(json_dict, f, indent=4)

with open(json_file_path, "r") as f:
    json_data = json.load(f)
print(json_data)

result_delimiter()

# ====================================================================================================

# buffering parameter
# The concept of "buffer" is not always easy. 
# If you saw the file for the previous print function, 
# I briefly explained the flush parameters. 
# Now let's move on to the "buffer" concept and summarize the changes in value. 
# 0 means not to use "buffer" and is only possible in binary files. 
# 1 means line buffering and is only possible in text files. 
# A positive value other than 1 means that you will use a buffer of that size and, 
# in the case of a negative number, you will use a system default.

# It won't be a lot of use, but it's expected to be used occasionally in projects dealing with large data files. 
# If I don't know the size of the file I have to deal with, I think it will be useful when I need to set up a suitable buffer for efficiency.
print(f"Default buffer size : {io.DEFAULT_BUFFER_SIZE}")

with open(get_path("datasets", "005_text.txt"), mode="r", buffering=3) as f:
    print(f.line_buffering)
    file_contents = f.buffer
    
    for line in file_contents:
        print(line)

result_delimiter()

# ====================================================================================================

# error parameter
# The error parameter defines how the error is handled in the context of encoding and decoding.


# 'strict' : Causes a ValueError exception if there is an encoding error. Default None has the same effect.

# 'ignore' : Ignore error. Please note that ignoring encoding errors can result in data loss.

# 'replace' : insert an alternate marker (such as '?') where invalid data is present.

# 'surrogateescape' : Indicates incorrect byte as code point in Unicode personal use area from U+DC80 to U+DCFF. 
#                     When the Surrogateescape error handler is used to write data, these private code points revert to their original bytes. 
#                     Useful when processing files with unknown encoding.

# 'xmlCharrepreplace' : Only supported when writing to a file. 
#                       Characters that are not supported by encoding are replaced with appropriate XML character references &#nnn; .

# 'backslashreplace' : Replaces invalid data with reverse slash escape sequence in Python.

# 'namereplace' : \N{...} Replace with escape sequence. Only supported when writing to a file.

# ====================================================================================================

# newline parameter
# Define how to add new lines. 
# This applies only to text files. 
# Available values can be None, Empty String, \n, \r, \r\n. 
# None uses the system's default line separator. 
# Empty character columns do not convert the end of the line, 
# and the remaining values use the given string. 
# Note that \n on Unix-of-line, \r\n on Windows, and \r on previous Macintosh.
print(f"System default line separator : {repr(os.linesep)}")
text_data_path = get_path("datasets", "005_text.txt")

with open(text_data_path, mode="r", newline="") as f:
    print(repr(f.read()))

print()

with open(text_data_path, mode="r", newline=None) as f:
    print(repr(f.read()))

result_delimiter()

# ====================================================================================================

# closefd parameter
# The closefd parameter is used when using the file descriptor. 
# The value of closefd is true and false, 
# but there is no problem with its operation except when close() is used in text_file_handle at the end. 
# If you delete a line that has a close() that causes an exception, there may seem to be no problem. 
# But in reality, that's not. 
# It is important to always close() the resource through connection with the outside, 
# but if closefd is true, the handle does not close and does not close at the same time. 
# So it is important to close the handle after setting it to Flase.
text_file_handle = open(get_path("datasets", "005_closefd.txt"), "r+")
file_descriptor = text_file_handle.fileno()

print(f"File descriptor : {file_descriptor}")

file_descriptor_object = open(file_descriptor, "a", closefd=False)
file_descriptor_object.write("closefd example\n")

file_descriptor_object.close()
text_file_handle.close()

result_delimiter()

# ====================================================================================================

# Example of handling binary files
text = "Hello Open Function"
with open(get_path('datasets', '005_binary_ex.bin'), mode="wb+") as f:
    encoded_text = text.encode("utf-8")
    f.write(encoded_text)
    f.seek(0)
    binary_data = f.read()
    print(f"binary data : {binary_data}")
    for byte in binary_data:
        print(f">>> byte : {byte}")
    decoded_data = binary_data.decode("utf-8")
    print(f"decoded data : {decoded_data}")

result_delimiter()

# ====================================================================================================

# Python File Object Attributes

with open(get_path("datasets", "005_text.txt")) as f:
    print(f"Name of the file : {f.name}")
    print(f"Is file closed : {f.closed}")
    print(f"mode : {f.mode}")
    print(f"encoding : {f.encoding}")

result_delimiter()

# ====================================================================================================

# Python File Object Methods

with open(get_path("datasets", "005_method_ex.txt"), "w+") as f:
    f.write("""Great talent is important in your field and explosive growth is also important.
    But more importantly, you never give up.
    Eventually, the winner stands at the end.""")
    f.seek(0)
    print(f.read())
    print(f"Is readable : {f.readable()}")
    print(f"Is writable : {f.writable()}")
    print(f"File descriptor (file no) : {f.fileno()}")
    print(f"Is connected to tty-like device : {f.isatty()}")
    f.truncate(10)
    f.flush()
    f.seek(0)
    print(f.read())
