import sys

class SnakeCharmer:
  def findSolution(self, N, V, snake):
      
    names = ['D','L','U','R']  
  
    n=N*N-1
    moves=['']*n
    
    d=0
    L=1
    i=0
    while i<n:

      for k in range(L):
        if i>=n: break
        moves[i]=names[d]
        i+=1      
      d=(d+1)%4
      
      for k in range(L):
        if i>=n: break
        moves[i]=names[d]
        i+=1      
      d=(d+1)%4
      L+=1
        
    return moves




N = int(input())
V = int(input())
snake = input()

prog = SnakeCharmer()
ret = prog.findSolution(N, V, snake)
print(len(ret))
for st in ret:
  print(st)
sys.stdout.flush()