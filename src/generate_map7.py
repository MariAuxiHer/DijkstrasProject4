import numpy as np
from numpy import random
import sys
import os, subprocess
from time import time
import tempfile
import tracemalloc
import re

def input_generator(number_inputs):
    tiles = ['f', 'g', 'G', 'h', 'm', 'r']
    size = number_inputs*number_inputs
    counter = 0


    # creating tmp files
    # tmp = tempfile.NamedTemporaryFile()
    os.chdir('../data')
    #with open(tmp.name, 'w') as input_file:
    with open(f'input{number_inputs}x{number_inputs}.txt', 'w') as input_file:
        # I think you may be able to create another file, read from this and then append it.. although you'll be creating more files, which 
        # will waste memory I guess....
        input_file.write(str(6) + "\n")
        input_file.write(str('f') + " " + str(3) + "\n")
        input_file.write(str('g') + " " + str(1) + "\n")
        input_file.write(str('G') + " " + str(2) + "\n")
        input_file.write(str('h') + " " + str(4) + "\n")
        input_file.write(str('m') + " " + str(7) + "\n")
        input_file.write(str('r') + " " + str(5) + "\n")
        input_file.write(str(number_inputs) + " " + str(number_inputs) + "\n")
        for current_val in range(size):
            if ((counter + 1)%(number_inputs)) == 0:
                input_file.write(str(random.choice(tiles)) + "\n")
            else: 
                input_file.write(str(random.choice(tiles)) + " ")
            counter += 1
        input_file.write(str(random.randint(0,1)) + " " + str(random.randint(0, 1)) + "\n")
        #input_file.write(str(random.randint(2, number_inputs-1)) + " " + str(random.randint(2, number_inputs-1)) + "\n")
        input_file.write(str(number_inputs-1) + " " + str(number_inputs-1) + "\n")
        #print(tempfile.gettempdir())

        #a = geek.zeros([5, 2], dtype = int)
        #a[0][1] = 3
        bytes_array = np.zeros(5)
        seconds_array = np.zeros(5)
        seconds = "seconds"
        word_bytes = "bytes"
        average_seconds = 0
        average_bytes_used = 0

            #bytes_allocated_characters = bytes_allocated_characters.replace(',', '')
            #bytes_used = int(bytes_allocated_characters)
            #print(f"bytes_used {bytes_used}")

            #average_seconds += end
            #average_bytes_used += bytes_used
    
        #average_seconds /= 5
        #average_bytes_used =  int(average_bytes_used/5)

        #print(f"| {number_inputs:<14}| {average_seconds:.4f} {seconds:<7}| {average_bytes_used} {word_bytes:<9}|")

        #print(f"| {number_inputs:<14}| {average_seconds:.4f}")
        #print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 
        
    input_file.close()


        # Now check the bytes allocated stuff AND time to see if it's properly working....
        # run 5 trials
    word_seconds = "seconds"
    word_bytes = "bytes"
    average_seconds = 0
    average_bytes_used = 0
    counter_bytes = 0; 
    counter_seconds = 0
    for current_val in range(5):
        input_file = open(f"input{number_inputs}x{number_inputs}.txt", "r")
        VALGRIND_ARGUMENTS = [
            'valgrind',
            '--leak-check=full',
            '../src/dijkstras'
        ]
            #start = time()
            #tracemalloc.start()
            # Runs program and redirects output to /dev/null
            #subprocess.run(["./dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)     
            #end = time() - start

            # Run valgrind.
            #start = time()
        process = subprocess.Popen(VALGRIND_ARGUMENTS, stdin=input_file, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL) 
            #process = subprocess.Popen(command, stderr=subprocess.PIPE)
        code = process.wait()
        errors = process.stderr.readlines() 
            #end = time() - start
        
        bytes_allocated_characters = ""
        for line in errors:
                #print(line)

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
                    #print("FOOOOOOOOUND")
                #print(bytes_allocated.group(0))
                    bytes_allocated_string = str(bytes_allocated.group(0))
                    for character in bytes_allocated_string:
                        if (character.isnumeric() or character == ','):
                            bytes_allocated_characters += character

            #print(f"\nbytes_allocated_characters {bytes_allocated_characters}\n")

        bytes_allocated_characters = bytes_allocated_characters.replace(',', '')
        bytes_used = int(bytes_allocated_characters)
            #print(f"bytes_used {bytes_used}")
        bytes_array[counter_bytes] = bytes_used
        counter_bytes += 1
            #average_seconds += end
            #average_bytes_used += bytes_used

            #print(f"average_bytes_used {average_bytes_used}")

    #print(os.getcwd())
    for current_val in range(5):
        input_file = open(f"input{number_inputs}x{number_inputs}.txt", "r")
        start = time()
        subprocess.run(["../src/dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)
            #process = subprocess.Popen(command, stderr=subprocess.PIPE)
        end = time() - start
        seconds_array[counter_seconds] = end
        counter_seconds += 1

    for seconds in seconds_array:
        average_seconds += seconds
        #print(seconds)

    for bytes in bytes_array:
        average_bytes_used += bytes
        #print("bytes")
        #print(bytes)

    #print("seconds")
    #print(average_seconds)
    average_seconds /= 5
    #print(average_seconds)
    average_bytes_used = int(average_bytes_used/5)
    #print(average_bytes_used)

    print(f"| {number_inputs:<14}| {average_seconds:.4f} {word_seconds:<7}| {average_bytes_used} {word_bytes:<8}|")

    #print(f"| {number_inputs:<14}| {average_seconds:.4f}")
    print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 

if __name__ == "__main__":
    # input_generator(10)
    # store these in an array, loop through the array, and pass it to input_generator 10, 20, 50, 100, 200, 500, 1000
    n = "N"
    elapsed_time = "Elapsed Time"
    memory_usage = "Memory Usage"
    print(f"| {n:<14}| {elapsed_time:<14}| {memory_usage:<14}|")
    print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 
    arr = np.array([10, 20, 50, 100, 200, 500, 1000])
    #arr = np.array([10])
    #arr = np.array([4, 5, 20])
    for number_inputs in arr:
        input_generator(number_inputs)