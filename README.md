# Programming-Assignment-2-Greedy-Algorithms

### Kevin Jin, 24470226
### Keerat Kohli, 41823869

To run our code, run from main.py in the src folder.

Upon running, user will be prompted to run either "custom" or "standard" tests. Please type the desired mode exactly as it appears to select. 

Standard tests are three nontrivial input files that have been used to answer the questions stored in the tests folder. The result will be returned in the corresponding output files in the tests folder.

To run user-defined tests, select custom mode and create an input.in file in the data folder with the correct format. The result will be returned in an output.out file in the data folder. The results will also be printed. An example input.in and output.out file has already been provided.

Both modes assume that the file input is in the following format:

k m

r_1 r_2 r_3 ... r_m

Where k is cache capacity with k >= 1, m is number of requests and r_1, .., r_m is sequence of integer IDs.

The output gives the number of misses for FIFO, LRU and OPTFF cache eviction policies.
