# open() - returns a file object, which has a read() method
# open(file, mode='r') - opens a file in read mode
#  - file: The file to be opened.
#  - mode: The mode to open the file:
#     - 'r' for read, 'w' for write, 'a' for append.

read_stream = open("test.txt", "r")

# read() - reads the entire file
# read(chars) - reads the specified number of chars
# print(read_stream.read())

# readline() - reads the next line
# readline(chars) - reads the specified number of chars
print(read_stream.readline())

# readlines() - reads the entire file and returns a list of lines
print(read_stream.readlines())

# close() - closes the file
# read_stream.close()
# read_stream.close()

# flush() - flushes the write buffer
# read_stream.flush()

# readable() - returns True if the file is open for reading
print(read_stream.readable())