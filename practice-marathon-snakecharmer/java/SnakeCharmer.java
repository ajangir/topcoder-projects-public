import java.io.*;

public class SnakeCharmer
{
  public char[] findSolution(int N, int V, String snake)
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

  
  public static void main(String[] args) {
  try {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int N = Integer.parseInt(br.readLine());
    int V = Integer.parseInt(br.readLine());
    String snake = br.readLine();
    
    SnakeCharmer prog = new SnakeCharmer();
    char[] ret = prog.findSolution(N, V, snake);

    System.out.println(ret.length);
    for (int i = 0; i < ret.length; ++i) {
        System.out.println(ret[i]);
    }        
  }
  catch (Exception e) {}
  }
}