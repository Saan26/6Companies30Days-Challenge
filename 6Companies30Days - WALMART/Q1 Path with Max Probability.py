# Path with Maximum Probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for i, (s,e) in enumerate(edges):
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))
        probs = {i:0 for i in range(n)}
        seen = set()
        pq = [(-1, start)]
        
        while pq:
            prob, node = heapq.heappop(pq)
            seen.add(node)
            
            for neigh, nextprob in graph[node]:
                newprob = prob * nextprob
                
                if newprob < probs[neigh]:
                    probs[neigh] = newprob
                    heapq.heappush(pq, (newprob, neigh))
        return -probs[end]
            