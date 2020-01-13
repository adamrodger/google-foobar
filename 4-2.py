def solution(matrix, timer):
    """
    Notes:
        - This sounds a lot like the Travelling Salesman Problem, except with a time limit and negative time allowed
        - If you can find a loop which is always negative overall, you've essentially got infinite time so you can collect all bunnies
            - Work out how to detect this and then just return all bunnies
        - Should be able to do a BFS by taking all the paths out of the current location (there aren't that many)
            - state = (current.location, collected as string?, timer)
                - make sure data structure for collected copies between states instead of passing reference
            - for next in current.vertices: queue.push((next.location, collected + next.id, timer - next.cost))
            - Stop when:
                - we've collected everything and made it to the bulkhead
                - timer is negative and there's no negative path out - we're locked in :)
                     - unless bulkhead -> target costs n, then target back to bulkhead costs-n so it's a 'free' trip
                     - if bulkhead -> target -> bulkhead is net-negative then we've got a negative loop so don't need to deal with that in BFS
        - Should be able to adapt ideas from Advent of Code stuff - create a graph with vertices/costs, queue neighbours
        - While looking at Dijkstra stuff, found https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm which mentions this is better
          than Dijktra for dense graphs (i.e. where every node is connected to every other like this one)
    """
    return None

if __name__ == "__main__":
    print solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
    print solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
    