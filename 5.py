# Notes:
# - https://www.youtube.com/watch?v=wdDF7_vfLcE
#     - this video was incredibly helpful
#     - a standard 2D grid can be rotated or reflected 8 ways  - 4 rotations, where 1 rotation is the 'do nothing'
#       rotation and 4 reflections (horizontel, vertical and 2 diagonals)
#         - So G = 8 in orbit/stabilizer notation
#         - for the real problem, G isn't always 8 because we're allowed to do "any number of column or row swaps"
#           which is factorial
#     - for some configurations of the grid, all 8 of those produce a unique grid, for some only 4 do, and
#       for the rest there's only 1, i.e. the grid is perfectly symmetrical so rotating/reflecting doesn't
#       change it
#     - by taking 1 member from each of those sets of 8s, 4s and 1s, you end up with each truly unique
#       configuration of the grid with reflections/rotations ignored
# - https://en.wikipedia.org/wiki/Group_action_(mathematics)#Orbits_and_stabilizers
#     - How many configurations of a grid are 'fixed' - i.e. those that are equivalent after a given rotation/reflection
#     - this is what we're trying to count - how many 'equivalent' grids there are
# - https://en.wikipedia.org/wiki/Burnside%27s_lemma
#     - the number of orbits is equal to the average number of fixed grids
# - then this video series applies it to an 8x8 grid and starts talking about cycles: https://www.youtube.com/watch?v=IzFx7xZgryQ
# - https://en.wikipedia.org/wiki/Cyclic_permutation
#     - for each row/column, we need to pick the permutations of different colours - e.g. with width or height 4 we could
#       have them all the same, all different, or a mix of colours, e.g. partitions(4) = [(1,1,1,1), (1,1,2), (2,2), (1,3), (4)]
#     - those are the partitions of 4 (like in level 3-3, but allowing the 1-size partition)
#     - some of those will be fixed and some won't - e.g. the (4) partition is fixed for every element of G because they're all the same
#     - so n for use in Burnside's Lemma is the sum of all cycles for all row and column partitions (I think...)

from collections import Counter
from fractions import gcd
from math import factorial

def partitions(n, I=1):
    """
    All partitions of a number, i.e. the different ways you can add up smaller numbers to make that number
    e.g. partitions(4) = [(1,1,1,1), (1,1,2), (2,2), (1,3), (4)]
    From https://stackoverflow.com/a/44209393
    """
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def cycles(partition, n):
    """
    Find how many cycles there are for the given partition and row/column size n
    """
    # start with just every combination of the cells in the column/row
    cycles = factorial(n)

    # reduce the cycles down to only those which are distinct
    for colour, count in Counter(partition).items():
        cycles //= (colour**count) * factorial(count)

    return cycles

def solution(w, h, s):
    """
    A worked example for (2,2,2):

    G = 2!2! = 4
    partitions(2) = [(2), (1,1)]

    | grid pattern | row cycles | column cycles | colour combinations |
    | (2) (2)      | 1          | 1             | 2^2 = 4             |
    | (2) (1,1)    | 1          | 2             | 2^2 = 4             |
    | (1,1) (2)    | 2          | 1             | 2^2 = 4             |
    | (1,1) (1,1)  | 2          | 2             | 2^4 = 16            |

    n = 4 + 4 + 4 + 16 = 28

    n / G = 28 // 4 = 7
    """
    # G is the number of actions (rotations/reflections) which can be performed on the w*h grid
    # i.e. the number of possible column swaps multiplied by the number of possible row swaps
    G = factorial(w) * factorial(h)

    # n is the total number of colour combinations for the number of cycles in each combination of row/column
    n = 0

    for row_configuration in partitions(w):
        for column_configuration in partitions(h):
            row_cycles = cycles(row_configuration, w)
            column_cycles = cycles(column_configuration, h)
            configuration_cycles = row_cycles * column_cycles
            colour_combinations = s**sum([sum([gcd(r, c) for r in row_configuration]) for c in column_configuration])
            n += configuration_cycles * colour_combinations

    # Burnside's Lemma says the orbit count is equal to the average of the cycle counts of each action in G
    return str(n // G)

if __name__ == "__main__":
    #print solution(3, 3, 2) # 23, from the video - doesn't count because that's using 8 reflections/rotations where we're using row/column swaps
    print solution(2, 2, 2) # 7, from the first example
    print solution(2, 3, 4) # 430, from the second example
    print solution(12, 12, 20) # biggest possible from the problem text
