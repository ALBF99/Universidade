
public class ArrayStack<T> implements Stack<T>{

	int size;
    int top = 0;
    T[] pilha;
	
	@Override
	public void push(T elemento) {
		pilha[top] = elemento;
		top++;
		
	}

	@Override
	public T peek() {
		
	
		return pilha[top-1];
	}

	@Override
	public T pop() {
		
		
		T elementoRemovido = pilha[top-1];
		top--;
		return elementoRemovido;
		
	}

	@Override
	public int size() {
		
		return top++;
	}

	@Override
	public boolean empty() {
		
		if (top == 0) {
			return true;
		} else {
			return false;
		}
	}
	
	   public ArrayStack(int s) {
	        size = s;
	        this.pilha = (T[])new Object[size];
	        
	    }

}
