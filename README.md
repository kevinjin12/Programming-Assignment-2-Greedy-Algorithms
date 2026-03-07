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
Yes, such a sequence exists. Take the following sequence of 6 requests with cache capacity 3:

1 2 3 4 1 2

For FIFO: 

| Request | Cache After | Result
| --- | --- | --- |
| 1 | 1 | Miss |
| 2 | 1 2 | Miss |
| 3 | 1 2 3 | Miss |
| 4 | 2 3 4 | Miss |
| 1 | 3 4 1 | Miss |
| 2 | 4 1 2 | Miss |

We can see that there are 6 misses.

For OPTFF:

| Request | Cache After | Result
| --- | --- | --- |
| 1 | 1 | Miss |
| 2 | 1 2 | Miss |
| 3 | 1 2 3 | Miss |
| 4 | 1 2 4 | Miss |
| 1 | 1 2 4 | Hit |
| 2 | 1 2 4 | Hit |

We can see that there are only 4 misses. OPTFF evicts 3 in request 4 because page 3 is never used again.

So there is a sequence in which OPTFF incurs strictly fewer misses than FIFO.

