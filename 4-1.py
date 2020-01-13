from itertools import combinations

def solution(num_buns, num_required):
    """
    approach:
    - you have n bunnies
    - you require exactly r bunnies in order to open the doors (i.e. there are that many consoles)
        - r choose k is combinatorics - learned that in Project Euler :)
    - so, each key must have n-r+1 copies - e.g. n=2 and r=2 == 1 copy of each key, which makes sense becaue it's [[0], [1]]
        - the example with n=5, r=3 makes that clearer - each key appears exactly 3 times (5-3+1)
    - so, for each combination of r bunnies, make sure that combination has a key that no other combination has
    """
    bunnies = [[] for bunny in xrange(num_buns)]

    # divide the bunnies into group combinations - i.e. each bunny will appear in multiple groups
    groups = combinations(bunnies, num_buns - num_required + 1)

    for key, group in enumerate(groups):
        for bunny in group:
            # everyone in that group gets the key
            bunny.append(key)

    return bunnies

if __name__ == "__main__":
    print solution(5, 3)