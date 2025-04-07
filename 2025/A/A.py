#by Alex Pham

import math
def find(i, parent):
    # Write the actual code logic here
    if parent[i] == i:
        return parent[i]

    parent[i] = find(parent[i], parent)
    return parent[i]

def union(i, j, parent):
    pi = find(i, parent)
    pj = find(j, parent)

    if pi == pj:
        return False

    parent[pi] = pj
    return True

t = int(input())
while t > 0:
    t -= 1
    S, P = map(int, input().split())

    # Create a list of coordinates from the input
    coords = []
    for i in range(P):
        x, y = map(int, input().split())
        coords.append((x, y))

    # Go through all possible pairs of points to create a set of edges
    edges = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            ax, ay = coords[i] 
            bx, by = coords[j]

            d = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
            edges.append((d, i, j))
    
    # Used Kruskal's Algorithm to create a minimum spanning tree
    parent = [i for i in range(P)]     
    edges.sort()
    connected = []

    for i, (d, a, b) in enumerate(edges):
        if union(a, b, parent):
            connected.append((d, a, b))

    # Label points connected to highest weights as satelight communication stations 
    visited = set()
    for d, a, b in connected[::-1]:
        visited.add(a)
        visited.add(b)
        
        if len(visited) >= S:
            break
    
    # Filter all edges where a and b that both have satelite communication links
    res = list(filter(lambda x: x[1] not in visited or x[2] not in visited, connected))
    print(format(res[-1][0], ".2f"))