#    Project4Dijkstras
#    Maria Hernandez 
#    Austin Gilbert

GitHub Repo Link: https://github.com/MariAuxiHer/DijkstrasProject4.git

1. Markdown table

| N             | Elapsed Time  | Memory Usage    |
|---------------|---------------|-----------------|
| 10            | 0.0022 seconds| 127044 bytes    |
| 20            | 0.0037 seconds| 260120 bytes    |
| 50            | 0.0152 seconds| 1206920 bytes   |
| 100           | 0.0585 seconds| 4608768 bytes   |
| 200           | 0.2538 seconds| 18250688 bytes  |
| 500           | 1.7417 seconds| 113904844 bytes |
| 1000          | 7.6277 seconds| 455725332 bytes |



2. About our generate_map.py file and how to run it:

- Our python file automates the benchmarking for our dijkstras path finding component recording the elapsed time and memory usage. If the only command line argument is the name of the executable, our program generates 7 txt files (for N = 10, 20, 50, 100, 200, 500, and 1000) each with NxN map of random tiles, then automates benchmarking for each of these (run 5 trials to calculate time elapsed and 5 trials to calculate memory usage and then average the results). If one additional command line argument is provided (N), we generate one txt file with NxN map of random tiles (this N provided in the command line needs to be an integer). If the user provides more than two command line arguments, our program immediately terminates. 

- To measure the time elapsed, we used the time() function from the python's time module, and call a subprocess that runs our dijkstras component. We run 5 trials per N and average the time elapsed. 

- To measure the memory usage we call a subprocess that runs Valgrind on our dijkstras component. After running valgrind, the program looks for the line in valgrind's output that says "total heap usage" and the memory usage would be the bytes allocated. We run 5 trials per N and average the memory usage. 
Caveat: Since we are running valgrind in a subrpocess from our python file to benchmark the memory usage, it takes a long time to run the five trials for N = 1000. Thus, even though the input1000x1000.txt file should be generated fairly quickly, it will take a long time to get the results of the benchmarking for N = 1000. 

- For our codes to work we need a data/ and a src/ directory inside a parent directory. The Makefile is supposed to be in the parent directory, and it would generate two executables dijkstras and generate_map inside the src/ directory when running make in the parent directory. Our generate_map should work if run from the parent directory by running ./src/generate_map or ./src/generate_map N, or if run from the src/ directory by running ./generate_map or ./generate_map N. When running any of these commands, our generate_map executable will create the specified input file(s) in the data/ directory. 

3. Answers to the three questions can be located in each student's writeup. 
