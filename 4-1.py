from itertools import combinations

def solution(num_buns, num_required):
    """
    approach:
    - you have n bunnies
    - you require exactly r bunnies in order to open the doors (i.e. there are that many consoles)
        - r choose k is combinatorics - learned that in Project Euler :)
    - so, k = n-r+1 - e.g. n=2 and r=2 == 1 copy of each key, which makes sense becaue it's [[0], [1]]
        - the example with n=5, r=3 makes that clearer - each key appears exactly 3 times (5-3+1)
        - 5 choose 3 == 10 so the keys are 0-9
    - so, for each combination of k bunnies, make sure that combination has a key that no other combination has
    """
    bunnies = [[] for bunny in xrange(num_buns)]

    # divide the bunnies into combinations of k size - i.e. each bunny will appear in multiple groups
    k = num_buns - num_required + 1
    groups = combinations(bunnies, k)

    # everyone in a group gets a key matching the group ID
    for key, group in enumerate(groups):
        for bunny in group:
            bunny.append(key)

    # fortunately this is already formatted properly for the required output
    return bunnies

if __name__ == "__main__":
    print solution(5, 3)