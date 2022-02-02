# open() - returns a file object, which has a read() method
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
#      closefd=True, opener=None)
#  - file: The file to be opened.
#  - mode: The mode to open the file:
#     - 'r' for read, 'w' for write, 'a' for append.

read_stream = open("test.txt", "r")
print(read_stream.read())