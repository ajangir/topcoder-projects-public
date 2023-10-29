import sys
from point import *
from collections import deque

class Solution:
    debug = False
    plants = []
    sprinklers = []
    waterSource = []
    N = C = P = T = Z = 0
    grid = []
    notIrrigated = set()
    def getInput(self):

        self.N = int(input())
        self.C = int(input())
        self.P = int(input())
        self.T = int(input())
        self.Z = int(input())
        self.grid = [[0 for x in range(self.N)] for y in range(self.N)]
        for r in range(self.N):
            for c in range(self.N):
                self.grid[r][c] = int(input())
        return
    
    def validPoint(self, p:Point) -> bool:
        xn = self.N
        return p.x >= 0 and p.x < xn and p.y >=0 and p.y < xn
    def lessDistance(self,p1,p2):
        return abs(p1.x-p2.x)**2+abs(p1.y-p2.y)**2 <= self.Z**2
    
    def findPlantsWaters(self):
        for i in range(self.N):
            for j in range(self.N):
                val = self.grid[i][j]
                p = Point(i,j)
                if val == cell.WATER.value:
                    self.waterSource.append(p)
                elif val == cell.PLANT.value:
                    self.plants.append(p)
                    self.notIrrigated.add(p)
        if self.debug:
            print('findPlantsWaters')
            print(len(self.plants), *self.plants)
            print(len(self.waterSource),*self.waterSource)
        return
    
    def allPointsCenter(self,p):
        z = self.Z
        ans = []
        for i in range(z+1):
            for j in range(z+1):
                valid = lambda x : self.validPoint(x) and self.lessDistance(p,x) and x != p
                k = Point(i,j)
                if valid(p+k): ans.append(p+k)
                if valid(p-k):ans.append(p-k)
                k = Point(i,-j)
                if valid(p+k):ans.append(p+k)
                if valid(p-k):ans.append(p-k)
        return list(set(ans))
    
    def findPotentialSprinklers(self):
        n = self.N
        grid = self.grid
        plants  = self.plants
        ans = []
        scoreGrid = [[0 for _ in range(n)] for _ in range(n)]

        for i in plants:
            scoreGrid[i.x][i.y] = -1
            points = self.allPointsCenter(i)

            for j in points:
                if grid[j.x][j.y] == cell.EMPTY.value:
                    scoreGrid[j.x][j.y] += 1
        #print(scoreGrid)
        for j in range(n):
            for k in range(n):
                if scoreGrid[j][k] > 0 and self.grid[j][k] in [cell.PIPE.value, cell.EMPTY.value]:
                    ans.append((scoreGrid[j][k],Point(j,k)))
        ans.sort(key=lambda x:-x[0])
        
        if self.debug:
            print('final sprinklers list')
            print(len(ans))
            for i in ans:
                print(*i,end= ' ')
            print()
        return ans
    
    def absDist(self,p1:Point,p2:Point):
        return abs(p1.x-p2.x)+abs(p1.y-p2.y)
    
    def ifNeeded(self,sprinkler:Point) -> bool:
        points = self.allPointsCenter(sprinkler)
        for p in points:
            if self.grid[p.x][p.y] == cell.PLANT.value and p in self.notIrrigated:
                return True
        return False
    
    def getCloseWaterPath(self,source:Point) -> Point:
        qu = deque()
        qu.append([source])
        n = self.N
        waterFound = lambda a : self.grid[a.x][a.y] in [cell.WATER.value,cell.PIPE.value]
        visited = [[False for _ in range(n)]for _ in range(n)]

        while qu:
            path = qu.popleft()
            src = path[-1]
            visited[src.x][src.y] = True
            if waterFound(src):
                return path
            for i in range(4):
                dd = Point(src.x + dx[i],src.y + dy[i])
                if self.validPoint(dd) and not visited[dd.x][dd.y] and self.grid[dd.x][dd.y] != cell.PLANT.value:
                    new_path = list(path)
                    new_path.append(dd)
                    qu.append(new_path)
        return []
    
    def layPipe(self,path):
        for j in path:
            if self.grid[j.x][j.y] == cell.EMPTY.value:
                self.grid[j.x][j.y] = cell.PIPE.value
        return
    
    def addSprinkler(self,sprinkler):
        points = self.allPointsCenter(sprinkler)
        for i in points:
            if i in self.notIrrigated:
                self.notIrrigated.remove(i)
        return

    def removeSteps(self,path):
        def is_straight(p1,p2,p3):
            return (p3.x-p1.x)*(p2.y-p1.y) == (p3.y-p1.y)*(p2.x-p1.x)
        if len(path) < 3:
            return path
        ans = [path[0]]
        for i in range(1,len(path)-1):
            if not is_straight(path[i-1],path[i],path[i+1]):
                ans.append(path[i])
        ans.append(path[-1])
        return ans

    def output(self):
        self.findPlantsWaters()
        sprinklers = self.findPotentialSprinklers()

        count = len(self.plants)
        output = []

        for i in sprinklers:
            if count <= 0:
                break

            sprinkler = i[1]
            if self.ifNeeded(sprinkler):
                count -= i[0]

                pathAllSteps = self.getCloseWaterPath(sprinkler)
                
                self.layPipe(pathAllSteps)

                path = self.removeSteps(pathAllSteps)
                for i in range(len(path)-1):
                    x,y = path[i],path[i+1]
                    output.append(f"P {x.x} {x.y} {y.x} {y.y}")
                if self.grid[sprinkler.x][sprinkler.y] == cell.PIPE.value:
                    self.addSprinkler(sprinkler)
                    output.append("S {} {}".format(sprinkler.x,sprinkler.y))
        return output

def main():
    solution = Solution()
    solution.getInput()
    out = solution.output()
    print(len(out))
    
    for i in out:
        print(i)
    
    sys.stdout.flush()
    return

if __name__ == "__main__":
    main() 
