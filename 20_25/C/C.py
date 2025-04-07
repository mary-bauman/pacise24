#by Alex Pham
import sys
import heapq
from collections import defaultdict

while True:
    n = int(sys.stdin.readline().strip())
    
    if n == 0:
        break
    
    hotels = set(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())

    # Go through adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        a, b, t = map(int, sys.stdin.readline().strip().split())
        adj[a].append((b, t))
        adj[b].append((a, t))

    q = []
    # State: (Distance, Time Remaining, Hotels Visited, Node)
    q.append((0, 600, 0, 1))
    dist = {node : float('inf') for node in adj}
    dist[1] = 0
    res = -1

    while q:
        distance, remaining, h, curr = heapq.heappop(q)
        if remaining <= 0:
            continue

        if curr == n:
            res = h
            continue
        
        for neighbor, weight in adj[curr]:
            n_dist = distance + weight
            n_remaining = remaining - weight if neighbor not in hotels else 600
            n_hotel = h + int(neighbor in hotels)
            
            if n_dist < dist[neighbor] and n_remaining > 0:
                dist[neighbor] = n_dist
                heapq.heappush(q, (n_dist, n_remaining, n_hotel, neighbor))
        
    print(res)