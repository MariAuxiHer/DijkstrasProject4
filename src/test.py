import subprocess
import sys
import re

#VALGRIND_ARGUMENTS = [
#  'valgrind',
#  '--leak-check=full',
#  './dijkstras'
#]

VALGRIND_ARGUMENTS = [
  'valgrind',
  '--leak-check=full',
  './dijkstras'
]

# Compute the command line.
input_file = open("../data/input10x10.txt", "r")
#!!!!!!!!!!!!1
#subprocess.run(VALGRIND_ARGUMENTS, stdin=input_file)  

# , stdout=subprocess.DEVNULL
#command = VALGRIND_ARGUMENTS + sys.argv[1:]

# Run valgrind.

process = subprocess.Popen(VALGRIND_ARGUMENTS, stdin=input_file, stderr=subprocess.PIPE) 
#process = subprocess.Popen(command, stderr=subprocess.PIPE)
code = process.wait()
errors = process.stderr.readlines() 
bytes_allocated_characters = ""
for line in errors:
    #print(line)
    #string_bytes = re.search(r"bytes allocated", line)

    bytes_allocated_one_million = re.search(b"\d+,\d+,\d+ bytes allocated", line)
            #bytes_allocated = re.search(b"\d+,\d+ bytes allocated", line)
            #print(bytes_allocated)
    if bytes_allocated_one_million:
                    #print("FOOOOOOOOUND")
                #print(bytes_allocated.group(0))
        bytes_allocated_string = str(bytes_allocated_one_million.group(0))
        for character in bytes_allocated_string:
            if (character.isnumeric() or character == ','):
                bytes_allocated_characters += character
                            
    else:
        bytes_allocated = re.search(b"\d+,\d+ bytes allocated", line)
            #bytes_allocated = re.search(b"\d+,\d+ bytes allocated", line)
            #print(bytes_allocated)
        if bytes_allocated:
            print("FOOOOOOOOUND")
                #print(bytes_allocated.group(0))
            bytes_allocated_string = str(bytes_allocated.group(0))
            for character in bytes_allocated_string:
                if (character.isnumeric() or character == ','):
                    bytes_allocated_characters += character
    #     r" bytes allocated
    #bytes_allocated = re.search(b"\d+,\d+ bytes allocated", line)
    #     print("hey")
    #print(bytes_allocated)
    #if bytes_allocated:
    #    print(bytes_allocated.group(0))
    #    bytes_allocated_string = str(bytes_allocated.group(0))
    #    for character in bytes_allocated_string:
    #        if (character.isnumeric() or character == ','):
    #            bytes_allocated_characters += character

print(f"bytes_allocated_characters {bytes_allocated_characters}")

bytes_allocated_int = int(bytes_allocated_characters.replace(',', ''))
print(f"bytes_allocated_int {bytes_allocated_int}")
print("YES! We have a match!")
