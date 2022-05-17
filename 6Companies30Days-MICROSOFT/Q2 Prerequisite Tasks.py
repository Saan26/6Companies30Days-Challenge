# Prerequisite Tasks----------------------------------------------

class Solution:
    def isPossible(self,N,prerequisites):
        adj = [[] for x in range(N)]
        for p in prerequisites:
            adj[p[1]].append(p[0]) 
        visited = [-1] * N
        onpath = [-1] * N
        for i in range(N):
            if visited[i] == -1:
                if self.dfs(i, adj, visited, onpath):
                    return False
        return True
    def dfs(self, i, adj, visited, onpath):
        if visited[i] != -1:
            return False
        visited[i] = 0
        onpath[i] = 0
        for ne in adj[i]:
            if onpath[ne] == 0:
                return True
            if self.dfs(ne, adj, visited, onpath):
                return True
        onpath[i] = -1
        return False
    