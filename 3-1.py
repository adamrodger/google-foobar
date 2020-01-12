def solution(n):
    n = long(n)
    count = 0

    while n > 1:
        if n % 2 == 0:
            n = n >> 1
            count += 1
        else:
            # decide whether it's more efficient to add or subtract
            # by checking which creates the longest chain of 0s in binary
            if (n > 3) and (n & 0b10):
                n += 1
            else:
                n -= 1
            count += 1
        
    return count

if __name__ == "__main__":
    tests = [
      ("4", 2),
      ("15", 5),
      ("1", 0),
      ("11", 5), # add 1, then go from 12
      ("12", 4), # between powers of 2
      ("13", 5), # subtract 1, then go from 12
      ("4294967295", 33), # 2^32 - 1
      ("4294967296", 32), # 2^32
      ("4294967297", 33), # 2^32 + 1
      ("18446744073709551615", 65), # 2^64 - 1
      ("18446744073709551616", 64), # 2^64
      ("18446744073709551617", 65), # 2^64 + 1
      ("36893488147419103232", 65), # 2^65
    ]
    
    for test, expected in tests:
        print "%s = %d, expected %d" % (test, solution(test), expected)
    