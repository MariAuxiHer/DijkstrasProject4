import numpy as np
from numpy import random
import sys
import os, subprocess
from time import time
import tracemalloc

def input_generator(number_inputs):
    #nxn_matrix = random.choice(['f', 'g', 'G', 'h', 'm', 'r'], size=(number_inputs, number_inputs))
    #print((counter + 1)%(nxn_matrix))
    tiles = ['f', 'g', 'G', 'h', 'm', 'r']
    size = number_inputs*number_inputs
    counter = 0

    # create the files in the data directory..
    os.chdir('../data')
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
        input_file.write(str(number_inputs-1) + " " + str(number_inputs-1) + "\n")
        #input_file.write(str(random.randint(2, number_inputs-1)) + " " + str(random.randint(2, number_inputs-1)) + "\n")


        # After creating the file, I want to create a subprocess, pass this file to the dijkstras executable and calculate the time. 
        print(os.getcwd())
        tracemalloc.start()
        start = time()
                # Runs program and redirects output to /dev/null
        subprocess.run(["../src/dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)
                
        end = time() - start
        print(f"{number_inputs} : elapsed time {end:.4f} seconds : Memory usage {tracemalloc.get_tracemalloc_memory()} bytes")
        
        tracemalloc.stop()
        input_file.close()

        # Deletes old test input file.
        #if os.path.exists("./test_vals.txt"):
        #   os.remove("./test_vals.txt")

        # I can try deleting the files later so that it doesnt occupy that much memory. 

if __name__ == "__main__":
    # input_generator(10)
    # store these in an array, loop through the array, and pass it to input_generator 10, 20, 50, 100, 200, 500, 1000
    # arr = np.array([10, 20, 50, 100, 200, 500, 1000])
    arr = np.array([4, 5, 20, 300, 1000])
    for number_inputs in arr:
        input_generator(number_inputs)


         n = "N"
    time = "Elapsed Time"
    #print(f"{n:<15}{time:<15}")
    #print(f"{n:<15}|Elapsed Time  |Memory usage")