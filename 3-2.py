def solution(m, f):
    # work backwards, subtracting smaller from larger until either
    #   - m and f are both 1
    #   - or, it's impossible because m == f (so m - f == 0)
    #   - or, it's impossible because m < 1 or f < 1
    m = long(m)
    f = long(f)
    count = 0

    while True:
        if 1 < f < m:
            count += (m / f)
            m = m % f
            
        if 1 < m < f:
            count += (f / m)
            f = f % m

        if m == 1 and f == 1:
            return str(count)
        elif m == f or m < 1 or f < 1:
            return "impossible"
        elif m == 1 and f > 1:
            return str(count + f - 1)
        elif f == 1 and m > 1:
            return str(count + m - 1)

if __name__ == "__main__":
    tests = [
        (("4", "7"), "4"),
        (("2", "1"), "1"),
        (("2", "4"), "impossible"),
        (("2", "2"), "impossible"),
        (("1", "1"), "0"),
    ]

    for args, expected in tests:
        print "%s = %s, expected %s" % (args, solution(*args), expected)