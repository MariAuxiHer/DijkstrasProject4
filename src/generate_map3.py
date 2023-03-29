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

        #a = geek.zeros([5, 2], dtype = int)
        #a[0][1] = 3
        multiple_runs = np.zeros([5, 2]) 
        seconds = "seconds"
        word_bytes = "bytes"
        counter_trials = 0
        counter_average = 0
        average_seconds = 0
        average_bytes_used = 0

        # run 5 trials
        for current_val in range(5):
            start = time()
            tracemalloc.start()
            # Runs program and redirects output to /dev/null
            subprocess.run(["./dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)      
            end = time() - start
            bytes_used = tracemalloc.get_tracemalloc_memory()
            tracemalloc.stop()
            #print(f"{number_inputs:<14} / {end:.4f} {seconds:<7} / {bytes_used} {word_bytes:<9}* ")
            average_seconds += end
            average_bytes_used += bytes_used
            #multiple_runs[counter_trials][0] = round(end,4)
            #multiple_runs[counter_trials][1] = round(bytes_used,4)
            #print("\nMatrix a : \n", multiple_runs)
            #counter_trials += 1

        print("\nTotal seconds : \n", average_seconds)
        print("\nTotal bytes : \n", average_bytes_used)
        average_seconds /= 5
        average_bytes_used =  int(average_bytes_used/5)

        print("\nTotal seconds : \n", average_seconds)
        print("\nTotal bytes : \n", average_bytes_used)

        #for current_val in multiple_runs:
        #    average_seconds += multiple_runs[counter_average][0]
        #    counter_average += 1
        print(f"| {number_inputs:<14}| {average_seconds:.4f} {seconds:<7}| {average_bytes_used} {word_bytes:<9}|")
        print(f"|{'-'*15}|{'-'*15}|{'-'*15}|") 
        
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