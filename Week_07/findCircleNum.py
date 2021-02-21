class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n,ans = len(isConnected),0
        visited = set()
        
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j]==1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans
