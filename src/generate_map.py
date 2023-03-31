#!/usr/bin/env python
#    Maria Hernandez 
#    Austin Gilbert
#    COSC302
#    03/31/2023
#    Project4
#    generate_map.py
#    This program generates NxN maps of random tiles, with the following values of N: 10, 20, 50, 100, 200, 500, 1000
#    Then, it benchmarks our dijkstras algorithm on each of these map sizes recording the elapsed time and memory usage.

# Importing modules
import numpy as np
from numpy import random
import os, subprocess
from time import time
import re
import sys

# Function to generate NxN maps of random tiles
def input_generator(number_inputs):
    tiles = ['f', 'g', 'G', 'h', 'm', 'r']
    size = number_inputs*number_inputs
    counter = 0

    # Changing directory to store the files in the ./data directory.
    os.chdir('../data')

    # Creating input files that contains NxN maps of random tiles, with the following values of N: 10, 20, 50, 100, 200, 500, 1000
    with open(f'input{number_inputs}x{number_inputs}.txt', 'w') as input_file:
        input_file.write(str(6) + "\n")
        input_file.write(str('f') + " " + str(3) + "\n")
        input_file.write(str('g') + " " + str(1) + "\n")
        input_file.write(str('G') + " " + str(2) + "\n")
        input_file.write(str('h') + " " + str(4) + "\n")
        input_file.write(str('m') + " " + str(7) + "\n")
        input_file.write(str('r') + " " + str(5) + "\n")
        input_file.write(str(number_inputs) + " " + str(number_inputs) + "\n")
        for _ in range(size):

            # Storing in the map a random value from the tiles array in each of the 0 - (NxN) positions.
            if ((counter + 1)%(number_inputs)) == 0:
                input_file.write(str(random.choice(tiles)) + "\n")
            else: 
                input_file.write(str(random.choice(tiles)) + " ")
            counter += 1
        input_file.write("0" + " " + "0" + "\n")
        input_file.write(str(number_inputs-1) + " " + str(number_inputs-1) + "\n")
    input_file.close()

    benchmark()

# Function to benchmarks our dijkstras algorithm on each of the map sizes recording the elapsed time and memory usage.
def benchmark():
    bytes_array: list[float] = []
    seconds_array: list[float] = []    
    word_seconds = "seconds"
    average_seconds = 0
    average_bytes_used = 0

    # Running 5 trials and averaging the results of the elapsed time and memory usage.
    for _ in range(5):

        # Opening the respective file.
        input_file = open(f"input{number_inputs}x{number_inputs}.txt", "r")

        # Call a subrprocess that runs our dijkstras executable. Calculate the time it takes to run this subprocess
        # with the time() function from the time module. Then, store the elapsed time of each trial in an array.
        start = time()
        subprocess.run(["../src/dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)
        end = time() - start
        seconds_array.append(end)

        # Reseting the file pointer to the beginning of the file before the second subprocess call.
        input_file.seek(0)

        # Setting up the commands to run valgrind on the subprocess. 
        VALGRIND_ARGUMENTS = [
            'valgrind',
            '--leak-check=full',
            '../src/dijkstras'
        ]

        # Create a subprocess that runs valgrind in our dijkstras.
        process = subprocess.Popen(VALGRIND_ARGUMENTS, stdin=input_file, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL) 
        code = process.wait()
        errors = process.stderr.readlines() 
        
        bytes_allocated_characters = ""

        # Searching the "total heap usage" in the valgrind's output to find the total bytes allocated (memory usage).
        for line in errors:
            bytes_allocated_one_million = re.search(b"total heap usage:.*?,\s*(\d[\d,]*)\s*bytes allocated", line)
            if bytes_allocated_one_million:
                bytes_allocated_string = str(bytes_allocated_one_million.group(1))
                for character in bytes_allocated_string:
                    if (character.isnumeric() or character == ','):
                        bytes_allocated_characters += character

        # Then, store the memory usage of each trial in an array.
        bytes_allocated_characters = bytes_allocated_characters.replace(',', '')
        bytes_used = int(bytes_allocated_characters)
        bytes_array.append(bytes_used)

    # Caluclate the average of all trials for both (elapsed time and memory usage), then print a markdown table.
    average_seconds = sum(seconds_array)/5
    average_bytes_used = int(sum(bytes_array)/5)
    average_bytes_string = str(average_bytes_used) + " bytes"
    print(f"| {number_inputs:<14}| {average_seconds:.4f} {word_seconds:<7}| {average_bytes_string:<17}|")
    print(f"|{'-'*15}|{'-'*15}|{'-'*18}|") 

if __name__ == "__main__":

    # Changing current working directory to the directory where this script is located.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Getting all the command-line arguments passed to the Python script.
    args = sys.argv
    num_of_args = len(args)

    # If you want to generate all the files at once (all maps with different NxN sizes), and then benchmark them:. 
    if num_of_args == 1:
    # Create an array with the the following N inputs: 10, 20, 50, 100, 200, 500, 1000
    # and call the input_generator function inside a for loop passing one input per iteration.
        n = "N"
        elapsed_time = "Elapsed Time"
        memory_usage = "Memory Usage"
        print(f"| {n:<14}| {elapsed_time:<14}| {memory_usage:<17}|")
        print(f"|{'-'*15}|{'-'*15}|{'-'*18}|") 
        arr = np.array([10, 20, 50, 100, 200, 500, 1000])
        for number_inputs in arr:
            input_generator(number_inputs)

    # If you want to generate each file individually (each map of size NxN separately), and then benchmark it: 
    elif num_of_args == 2:
        n = "N"
        elapsed_time = "Elapsed Time"
        memory_usage = "Memory Usage"
        print(f"| {n:<14}| {elapsed_time:<14}| {memory_usage:<17}|")
        print(f"|{'-'*15}|{'-'*15}|{'-'*18}|") 
        number_inputs = int(args[1])
        input_generator(number_inputs)
    
    # If provided more than two command line arguments:
    else: 
        sys.exit(1)