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

## Question 1

| Input File | k | m | FIFO | LRU | OPTFF |
| --- | --- | --- | --- | --- | --- |
| test1 | 3 | 50 | 31 | 32 | 19 |
| test2 | 8 | 50 | 28 | 30 | 21 |
| test3 | 7 | 50 | 25 | 23 | 16 |

From our test cases, we notice that OPTFF has the fewest number of misses in all test cases which confirms theoretical results. Additionally, compared to FIFO and LRU it is a significant improvement with around 33% less misses.

From our test cases, we see that LRU and FIFO have roughly the same number of cache misses. However, this may be because our data was randomly generated. LRU often performs better in the real world because recently accessed items are more likely to be accessed again.

## Question 2
Yes, such a sequence exists. Take the sequence used in test1 with cache capacity 3 and 50 requests:

4 4 5 1 2 4 4 3 6 2 1 5 4 3 1 2 6 3 1 4 2 5 3 4 4 3 6 3 4 2 6 3 6 3 2 4 2 4 5 4 1 5 1 2 2 2 3 5 3 2

This sequence has 19 cache misses for OPTFF and 32 cache misses for LRU and 31 cache misses for FIFO. OPTFF has strictly fewer cache misses than both LRU and FIFO.
