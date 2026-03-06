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

def optff(k, requests):
    next_indx = {}

    for indx, r in enumerate(requests):
        if r not in next_indx:
            next_indx[r] = deque()
        next_indx[r].append(indx)

    cache = set()
    misses = 0
    for r in requests:

        next_indx[r].popleft()

        if r in cache:
            continue

        misses += 1
        if len(cache) == k:
            req_with_furthest_indx = -1
            furthest_indx = -1

            for elem in cache:
                elem_next_indx = next_indx[elem][0] if next_indx[elem] else len(requests)
                if elem_next_indx > furthest_indx:
                    req_with_furthest_indx = elem
                    furthest_indx = elem_next_indx
            
            cache.remove(req_with_furthest_indx)
        
        cache.add(r)
    
    return misses
    
def main():
    file_path = "../tests/simple_test.in"
    output_path = "../tests/simple_test.out"

    with open(file_path, "r") as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)
    lru_misses = lru(k, requests)
    optff_misses = optff(k, requests)

    with open(output_path, "w") as f:
        f.write(f"FIFO  : {fifo_misses}\n")
        f.write(f"LRU   : {lru_misses}\n")
        f.write(f"OPTFF : {optff_misses}")

    print(f"FIFO  : {fifo_misses}")
    print(f"LRU   : {lru_misses}")
    print(f"OPTFF : {optff_misses}")

if __name__ == "__main__":
    main()