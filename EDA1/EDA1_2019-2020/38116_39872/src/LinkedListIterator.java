public class LinkedListIterator<T> implements java.util.Iterator<T> {

    private SingleNode<T> currentSingle;

    LinkedListIterator(SingleNode<T> c) {
        currentSingle = c;
    }

    public boolean hasNext() {
        return currentSingle != null;
    }

    public T next() {
        T nextItem;
        if (!hasNext())
            throw new java.util.NoSuchElementException();

        nextItem = currentSingle.element();
        currentSingle = currentSingle.getNext();
        return nextItem;
    }

    public void remove() {
        throw new UnsupportedOperationException();
    }


}