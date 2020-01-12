# approach:
# - run the simulation, keeping results in a hashset
# - when the hashset contains the result, you've entered a cycle
# - run the simulation until you get that same result again, counting the loop

def baseb(n, b):
    # convert a base-10 number to a base-n number
    # https://stackoverflow.com/a/39884219
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)

def calculate(n, k, base):
    # calculate the next element in the chain
    x = int("".join(sorted(n, reverse=True)), base)
    y = int("".join(sorted(n)), base)
    z = baseb(x - y, base).zfill(k) # convert back to base with leading zeroes
    return z

def solution(n, b):
    results = set()
    k = len(n)

    # iterate until we find the first element of the cycle
    while True:
        n = calculate(n, k, b)
        if n in results:
            break
        results.add(n)

    # now we're inside the loop, count elements until it repeats again
    count = 1
    end = n
    n = calculate(n, k, b)

    while n != end:
        count += 1
        n = calculate(n, k, b)

    return count

if __name__ == "__main__":
    print(solution('1211', 10))
    print(solution('210022', 3))