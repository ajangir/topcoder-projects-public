import sys
from point import *
from collections import deque

class Solution:
    debug = True
    plants = []
    sprinklers = []
    waterSource = []
    N = C = P = T = Z = 0
    grid = []

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
    
    def lessDistance(self, p1:Point, p2:Point):
        return abs(p1.x-p2.x)**2+abs(p1.y-p2.y)**2 <= self.Z**2

    def absDist(self,p1:Point,p2:Point):
        return abs(p1.x-p2.x)+abs(p1.y-p2.y)

    def findPlantsWaters(self):
        for i in range(self.N):
            for j in range(self.N):
                val = self.grid[i][j]
                if val == cell.WATER.value:
                    self.waterSource.append(Point(i,j))
                elif val == cell.PLANT.value:
                    self.plants.append(Point(i,j))
        if self.debug:
            print('findPlantsWaters')
            print(len(self.plants), *self.plants)
            print(len(self.waterSource),*self.waterSource)
        return
    
    def findPotentialSprinklers(self):
        n = self.N
        grid = self.grid
        plants  = self.plants
        ans = []
        scoreGrid = [[0 for _ in range(n)] for _ in range(n)]
        for i in plants:
            scoreGrid[i.x][i.y] = -1
            for j in range(n):
                for k in range(n):
                    if grid[j][k] == 0 and self.lessDistance(i,Point(j,k)):
                        scoreGrid[j][k] += 1
        for j in range(n):
            for k in range(n):
                if scoreGrid[j][k] > 0:
                    ans.append((scoreGrid[j][k],Point(j,k)))
        ans.sort(key=lambda x:-x[0])
        if self.debug:
            print('findPotentialSprinklers')
            print(len(ans))
            for i in ans:
                print(*i)
        return ans
    
    def distanceWater(self,sprinklers):
        n = self.N
        distance = [[[INF,Point(-1,-1)] for _ in range(n)] for _ in range(n)]
        ans = []
        for i in self.waterSource:
            distance[i.x][i.y] = [0,i]
            qu = deque()
            qu.append(i)
            while qu:
                source = qu.popleft()
                for j in range(4):
                    ddx,ddy = source.x + dx[j], source.y + dy[j]
                    if self.validPoint(Point(ddx,ddy)) and self.grid[ddx][ddy] == cell.EMPTY.value and \
                    distance[ddx][ddy][0] >= distance[source.x][source.y][0]+1:
                        distance[ddx][ddy] = [distance[source.x][source.y][0]+1,i]
                        qu.append(Point(ddx,ddy))
        for i in sprinklers:
            x,y = i[1].x,i[1].y
            val = [i[0],distance[x][y][0],distance[x][y][1],i[1]]
            ans.append(val)
        ans.sort(key = lambda x:(-x[0],x[1]))
        return ans
    
    def getCloseWaterPath(self,source:Point) -> Point:
        qu = deque()
        qu.append([source])
        n = self.N
        waterFound = lambda a : self.grid[a.x][a.y] in [cell.WATER.value,cell.PIPE.value, cell.SPRINKLER.value]
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
        sprinklers_with_distance = self.distanceWater(sprinklers)
        count = len(self.plants)
        output = []
        for i in sprinklers_with_distance:
            if count <= 0:
                break
            # from src = sprinkler, destination = water pipe or source
            sprinkler = i[3]
            count -= i[1]

            pathAllSteps = self.getCloseWaterPath(sprinkler)
            
            self.layPipe(pathAllSteps)

            path = self.removeSteps(pathAllSteps)
            for i in range(len(path)-1):
                x,y = path[i],path[i+1]
                output.append(f"P {x.x} {x.y} {y.x} {y.y}")
            
            output.append("S {} {}".format(sprinkler.x,sprinkler.y))
        return output
    
    def testFunc(self):
        s = [Point(2,3),Point(5,2),Point(3,1),Point(1,6)]
        def layPipe(s):
            if self.grid[s.x][s.y] == cell.EMPTY.value:
                self.grid[s.x][s.y] = cell.PIPE.value
        for i in s:
            path = self.getCloseWaterPath(i)
            print('i = ',i,*path)
            for j in path:
                layPipe(j)
            for j in self.grid:
                print(j)
        return
 
def main():
    solution = Solution()
    solution.getInput()
    out = solution.output()
    print(len(out))
    
    for i in out:
        print(i)
    
    #solution.testFunc()
    sys.stdout.flush()
    return

if __name__ == "__main__":
    main() 
