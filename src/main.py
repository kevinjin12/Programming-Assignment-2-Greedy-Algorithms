from collections import deque

def fifo(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for r in requests:
        if r in cache:
            continue

        misses += 1

        if len(cache) == k:
            evicted = order.popleft()
            cache.remove(evicted)

        cache.add(r)
        order.append(r)

    return misses


def main():
    file_path = "tests/test1.in"

    with open(file_path, "r") as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    fifo_misses = fifo(k, requests)

    print(f"FIFO  : {fifo_misses}")


if __name__ == "__main__":
    main()