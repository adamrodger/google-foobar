from itertools import permutations

def solution(matrix, timer):
    """
    Calculate the maximum number of bunnies that can be rescued and return their locations
    """
    floyd_warshall(matrix)

    if negative_loop(matrix):
        # shortcut calculation - all bunnies can be saved
        return list(range(len(matrix) - 2))
    else:
        return most_efficient_path(matrix, timer)

def floyd_warshall(matrix):
    """
    Find the shortest path between each pair of locations using the O(n^3) Floyd-Warshall algorithm:
    https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    """
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # pick shorter out of path from i->j or i->k->j
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix

def negative_loop(dists):
    """
    Check if the distance matrix contains a negative loop - i.e. you can get from some location back
    to that location again in negative time. You could just follow this loop many times until you got
    enough time to save all bunnies and exit
    """
    return any([dists[x][x] < 0 for x in range(len(dists))])
    
def most_efficient_path(dists, time_limit):
    """
    Given the pre-calculated shortest distances between pairs of nodes, find the most efficient path
    i.e. the one which saves the most bunnies
    """
    all_bunnies = list(range(len(dists) - 2))
    most_efficient = []

    # try every permutation of possible bunnies with length 1 to n and track longest permutation within time limit
    for r in range(1, len(all_bunnies) + 1):
        for p in permutations(all_bunnies, r):
            cost = get_path_cost(dists, p)

            if cost <= time_limit and r > len(most_efficient):
                most_efficient = list(p)
    
    return sorted(most_efficient)

def get_path_cost(dists, p):
    """
    Get the cost of the shortest path from start -> (bunny permutation) -> end
    """
    current = 0
    cost = 0

    # collect every bunny in order
    for bunny in p:
        cost += dists[current][bunny + 1]
        current = bunny + 1

    # go from the last bunny to the exit
    cost += dists[current][len(dists) - 1]
    return cost

if __name__ == "__main__":
    print solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
    print solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
