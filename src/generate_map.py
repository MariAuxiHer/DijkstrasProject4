import numpy as np
from numpy import random
import sys
import os, subprocess
from time import time
import tempfile
import tracemalloc

def input_generator(number_inputs):
    tiles = ['f', 'g', 'G', 'h', 'm', 'r']
    size = number_inputs*number_inputs
    counter = 0

    # creating tmp files
    tmp = tempfile.NamedTemporaryFile()
    with open(tmp.name, 'w') as input_file:
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

        start = time()
        # Runs program and redirects output to /dev/null
        tracemalloc.start()
        subprocess.run(["./dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)      
        end = time() - start
        bytes_used = tracemalloc.get_tracemalloc_memory()
        seconds = "seconds"
        word_bytes = "bytes"
        print(f"| {number_inputs:<14}| {end:.4f} {seconds:<7}| {bytes_used} {word_bytes:<9}|")
        print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 
        tracemalloc.stop()
        
        input_file.close()

if __name__ == "__main__":
    # input_generator(10)
    # store these in an array, loop through the array, and pass it to input_generator 10, 20, 50, 100, 200, 500, 1000
    n = "N"
    elapsed_time = "Elapsed Time"
    memory_usage = "Memory Usage"
    print(f"| {n:<14}| {elapsed_time:<14}| {memory_usage:<14}|")
    print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 
    arr = np.array([10, 20, 50, 100, 200, 500, 1000])
    #arr = np.array([4, 5, 20])
    for number_inputs in arr:
        input_generator(number_inputs)