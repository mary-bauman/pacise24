#by team Mill from Millersville

from heapq import *

n = int(input())
while n:
    hotel = list(map(lambda x: int(x) - 1, input().split()[1:]))
    m = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append([b, c])
        graph[b].append([a, c])
    best = [[10**20] * (11 * 60) for _ in range(n)]
    best[0][10 * 60] = 0
    heap = [[0, 0, 10 * 60]] # days, city, hour_left
    while heap:
        day, curr, hour = heappop(heap)
        for to, dist in graph[curr]:
            if dist > hour:
                continue
            left = hour - dist
            if day < best[to][left]:
                best[to][left] = day
                heappush(heap, [day, to, left])
            if to in hotel:
                if best[to][left] + 1 < best[to][10 * 60]:
                    best[to][10 * 60] = best[to][left] + 1
                    heappush(heap, [best[to][left] + 1, to, 10 * 60])
    ans = min(best[n - 1])
    print(ans if ans != 10**20 else -1)
    n = int(input())