class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])

        visited=set()
        res=0

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            visited.add((r,c))
            while q:
                r1,c2=q.popleft()
                for dirr,dirc in directions:

                    nr,nc=r1+dirr,c2+dirc

                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    res+=1

        return res