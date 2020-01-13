# Sources:
# https://en.wikipedia.org/wiki/Partition_(number_theory)
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# https://math.stackexchange.com/questions/146482/the-number-of-ways-to-write-a-positive-integer-as-the-sum-of-distinct-parts-with
# http://mathworld.wolfram.com/PartitionFunctionQ.html
# https://math.stackexchange.com/questions/1971870/partitions-into-at-least-two-distinct-parts

def solution(n):
    a = [0] * (n+1)
    a[0] = 1
    a[1] = 1

    # sum the partial products up to n
    for x in range(2, n + 1):
        for k in range(n, x - 1, -1):
            a[k] = a[k] + a[k-x]

    # -1 because this will include a 1-length partition which we don't want
    return a[n] - 1

if __name__ == "__main__":
    print solution(1)
    print solution(2)
    print solution(5)
    print solution(200)
