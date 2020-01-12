def build_lookup(numbers, parent, lookup = {}):
    # populate a lookup of node:parent by traversing the tree once
    node = numbers[-1]
    lookup[node] = parent
    
    radix = int((len(numbers) - 1) / 2)
    
    if radix > 0:
        build_lookup(numbers[0:radix], node, lookup)
        build_lookup(numbers[radix:-1], node, lookup)
    
    return lookup

def solution(h, q):
    numbers = list(range(1, 2**h))
    lookup = build_lookup(numbers, -1)
    results = []
    
    for target in q:
        parent = lookup[target] if target in lookup else -1
        results.append(parent)
        
    return results
    
if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))