from collections import deque

def fifo(k, requests):
    cache = set()
    first_in = deque()
    misses = 0

    for r in requests:
        # cache hit
        if r in cache:
            continue

        # cache miss
        misses += 1

        if len(cache) == k:
            elemented_evicted = first_in.popleft()
            cache.remove(elemented_evicted)

        first_in.append(r)
        cache.add(r)

    return misses

def lru(k, requests):
    cache = {}
    misses = 0

    for r in requests:
        # cache hit
        if r in cache:
            cache.pop(r)
            cache[r] = 1

        # cache miss
        else:            
            misses += 1

            if len(cache) == k:
                cache.pop(next(iter(cache))) # Get first inserted key (lru element) and remove it

            cache[r] = 1

    return misses

def main():
    file_path = "../tests/simple_test.in"
    output_path = "../tests/simple_test.out"

    with open(file_path, "r") as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru(k, requests)

    with open(output_path, "w") as f:
        f.write(f"FIFO  : {fifo_misses}\n")
        f.write(f"LRU   : {lru_misses}\n")

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")

if __name__ == "__main__":
    main()