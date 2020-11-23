package Tree;

/*
	
******************************
*** Implementation of Tree ***
******************************
	
	
| index | [0] [1] [2] [3] [4] [5] [6] [7] |
| data  |  x   A   B   C   D   E       F  |				     
				     
		
      A(1)    
     /   \
    B(2)  C(3)  
  /   \      \              left child's index = parent's index * 2 
 D(4)  E(5)   F(7)          right child's index = parent's index * 2 + 1

*/

public class TreeUsingArray
{
	static final int DEFAULT_SIZE = 10;
	String[] _arr = new String[DEFAULT_SIZE];
	int _root = 0;
	
	public TreeUsingArray(String data)
	{
		_arr[_root] = data;
	}
	
	public void SetLeft(int root, String data)
	{
		int targetIndex = root * 2 + 1; // left child's index = parent's index * 2
		
		if (_arr[root] == null)
		{
			System.out.println("no parent found");
			return;
		}
		
		_arr[targetIndex] = data;
	}
	
	public void SetRight(int root, String data)
	{
		int targetIndex = root * 2 + 2; // Right child's index = parent's index * 2 + 1
		
		if (_arr[root] == null)
		{
			System.out.println("no parent found");
			return;
		}
		
		_arr[targetIndex] = data;
	}
	
	public void PrintAll()
	{
		System.out.print("All tree's items : ");
		for (int i=0; i<DEFAULT_SIZE; i++)
		{
			if (_arr[i] != null) System.out.printf("%s ",_arr[i]);
			else System.out.printf("  ");
		}
	}
	
	public static void main(String[] args)
	{
		TreeUsingArray tree = new TreeUsingArray("A");
		
		tree.SetLeft(0, "B");		
		tree.SetLeft(1, "D");
		tree.SetRight(1, "E");
		
		tree.SetRight(0, "C");
		tree.SetRight(2, "F");
		tree.SetLeft(5, "G"); // no parent found
		
		tree.PrintAll();
	}
}
