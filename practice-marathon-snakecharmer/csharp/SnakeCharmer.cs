using System;
using System.Collections.Generic;

public class SnakeCharmer
{
  public char[] findSolution(int N, int V, string snake)
  {  
    char[] names = {'L','D','R','U'};  
  
    int n=N*N-1;
    char[] moves=new char[n];
    
    for (int i=0,dir=0,L=1; i<n; )
    {
      for (int k=0; k<L && i<n; k++,i++) moves[i]=names[dir];
      dir=(dir+1)%4;
      for (int k=0; k<L && i<n; k++,i++) moves[i]=names[dir];
      dir=(dir+1)%4;
      L++;
    }
    
    return moves;  
  }
  
  static void Main(string[] args)
  {
    int N = int.Parse(Console.ReadLine());       
    int V = int.Parse(Console.ReadLine());       
    string snake = Console.ReadLine();

    SnakeCharmer prog = new SnakeCharmer();
    char[] ret = prog.findSolution(N, V, snake);

    Console.WriteLine(ret.Length);
    for (int i = 0; i < ret.Length; ++i)
    {
      Console.WriteLine(ret[i]);
    }
  }
}