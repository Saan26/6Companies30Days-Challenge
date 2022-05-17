# Bridge edge in a graph --------------------------------------------------

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        
        par = [-1] * V
        disc = [0] * V
        low = [0] * V
        ans = [0]
        visit = [False] * V
       
        for i in range(V):
            if not visit[i]:
                self.DFSUtil(adj, i, [0], disc, low, par, ans, visit, c,d)
       
        return ans[0]
    def DFSUtil(self, adj, u, time, disc, low, par, ans, visit, c, d):
        
        visit[u] = True
        disc[u] = time[0]
        low[u] = time[0]
       
        time[0] += 1
       
        for v in adj[u]:
            if not visit[v]:
                par[v] = u
                self.DFSUtil(adj, v, time, disc, low, par, ans, visit, c, d)
               
                low[u] = min(low[u], low[v])
               
                if low[v] > disc[u]:
                    if (u == c and v == d) or (u == d and v == c):
                        ans[0] = 1
               
            elif v != par[u]:
                low[u] = min(low[u], low[v])