import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private Node first;
    private Node last;
    private int size = 0;

    private class Node {
        Item item;
        Node next;
        Node prev;
    }

    public Deque() {
        first = null;
        last = null;
    }

    public boolean isEmpty() {
        if (size == 0 && first == null && last == null) {
            return true;
        }

        if (size == 0 || first == null || last == null) {
            throw new IllegalStateException();
        }

        return false;
    }

    public int size() {
        return size;
    }

    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }

        boolean isEmpty = isEmpty();
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        first.prev = null;

        if (isEmpty) {
            last = first;
        } else {
            oldfirst.prev = first;
        }

        size++;
    }

    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }

        boolean isEmpty = isEmpty();
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.next = null;
        last.prev = oldlast;

        if (isEmpty) {
            first = last;
        } else {
            oldlast.next = last;
        }

        size++;
    }

    public Item removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException("The deque is empty, so there is nothing to remove");
        }

        Item item = first.item;
        first = first.next;

        if (first != null) {
            first.prev = null;
        } else {
            last = null;
        }

        size--;
        return item;
    }

    public Item removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException("The deque is empty, so there is nothing to remove");
        }

        Item item = last.item;
        last = last.prev;

        if (last != null) {
            last.next = null;
        } else {
            first = null;
        }

        size--;
        return item;
    }

    @Override
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
        private Node current;

        public DequeIterator() {
            current = first;
        }

        @Override
        public boolean hasNext() {
            return current != null;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        @Override
        public Item next() {
            if (current == null) {
                throw new NoSuchElementException("You've reached the end of the deque");
            }
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    /**
     * purposefully empty
     * @param args contains nothing
     */
    public static void main(String[] args) {
    }
}
