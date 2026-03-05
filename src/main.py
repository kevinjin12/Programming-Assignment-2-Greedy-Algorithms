from collections import deque

def fifo(k, requests):
    cache = deque()
    misses = 0

    for r in requests:
        # cache hit
        if r in cache:
            continue

        # cache miss
        misses += 1

        if len(cache) == k:
            cache.popleft()

        cache.append(r)

    return misses

def lru(k, requests):
    cache = deque()
    misses = 0

    for r in requests:
        # cache hit
        if r in cache:
            cache.remove(r)
            cache.append(r)

        # cache miss
        else:            
            misses += 1

            if len(cache) == k:
                cache.popleft()

            cache.append(r)

    return misses

def main():
    file_path = "tests/test1.in"

    with open(file_path, "r") as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru(k, requests)

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")


if __name__ == "__main__":
    main()