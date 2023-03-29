import numpy as np
from numpy import random
import os, subprocess
from time import time
import re

def input_generator(number_inputs):
    tiles = ['f', 'g', 'G', 'h', 'm', 'r']
    size = number_inputs*number_inputs
    counter = 0

    os.chdir('../data')
    with open(f'input{number_inputs}x{number_inputs}.txt', 'w') as input_file:
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
        
    input_file.close()
    benchmark()

def benchmark():
    bytes_array: list[float] = []
    seconds_array: list[float] = []    
    word_seconds = "seconds"
    word_bytes = "bytes"
    average_seconds = 0
    average_bytes_used = 0

    for current_val in range(5):
        input_file = open(f"input{number_inputs}x{number_inputs}.txt", "r")

        start = time()
        subprocess.run(["../src/dijkstras"], stdin=input_file, stdout=subprocess.DEVNULL)
        end = time() - start
        seconds_array.append(end)

        input_file.seek(0)

        VALGRIND_ARGUMENTS = [
            'valgrind',
            '--leak-check=full',
            '../src/dijkstras'
        ]

        process = subprocess.Popen(VALGRIND_ARGUMENTS, stdin=input_file, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL) 
        code = process.wait()
        errors = process.stderr.readlines() 
        
        bytes_allocated_characters = ""
        for line in errors:
            bytes_allocated_one_million = re.search(b"total heap usage:.*?,\s*(\d[\d,]*)\s*bytes allocated", line)
            if bytes_allocated_one_million:
                #print(bytes_allocated_one_million.group(1))
                bytes_allocated_string = str(bytes_allocated_one_million.group(1))
                for character in bytes_allocated_string:
                    if (character.isnumeric() or character == ','):
                        bytes_allocated_characters += character

        bytes_allocated_characters = bytes_allocated_characters.replace(',', '')
        bytes_used = int(bytes_allocated_characters)
        bytes_array.append(bytes_used)

    average_seconds = sum(seconds_array)/5
    average_bytes_used = int(sum(bytes_array)/5)
    average_bytes_string = str(average_bytes_used) + " bytes"
    print(f"| {number_inputs:<14}| {average_seconds:.4f} {word_seconds:<7}| {average_bytes_string:<17}|")
    print(f"|{'-'*15}|{'-'*15}|{'-'*18}|") 

if __name__ == "__main__":
    n = "N"
    elapsed_time = "Elapsed Time"
    memory_usage = "Memory Usage"
    print(f"| {n:<14}| {elapsed_time:<14}| {memory_usage:<17}|")
    print(f"|{'-'*15}|{'-'*15}|{'-'*18}|") 
    arr = np.array([10, 20, 50, 100, 200, 500, 1000])
    for number_inputs in arr:
        input_generator(number_inputs)