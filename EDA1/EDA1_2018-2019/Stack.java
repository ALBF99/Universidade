import java.util.EmptyStackException;

public interface Stack <T>  {
    void push (T elemento);
    T peek() ;
    T pop() ;
    int size();
    boolean empty();
}
