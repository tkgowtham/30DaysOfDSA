import java.util.* ;
import java.io.*; 
public class Solution {

	public static void sortStack(Stack<Integer> stack) {
		// Write your code here.
		sort(stack);
	}

	public static void sort(Stack<Integer> s) {
		if (!s.isEmpty()) {
			int x = s.pop();
			sort(s);
			insert(s, x);
		}
	}

	public static void insert(Stack<Integer> s, int x) {
		if (s.isEmpty() || x > s.peek()) {
			s.push(x);
			return;
		}

		int temp = s.pop();
		insert(s, x);
		s.push(temp);
	}

}
