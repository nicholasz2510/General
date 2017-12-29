import java.util.Iterator;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    Item[] rq;
    private int head = 0;
    private int tail = 0;

    public RandomizedQueue() {
        rq = (Item[]) new Object[1];
        // TODO
    }

    public boolean isEmpty() {
        // TODO
        return true;
    }

    public int size() {
        // TODO
        return 0;
    }

    public void enqueue(Item item) {
        // TODO
    }

    public Item dequeue() {
        // TODO
        return null;
    }

    public Item sample() {
        // TODO
        return null;
    }

    @Override
    public Iterator<Item> iterator() {
        return new ListIterator();
    }

    private class ListIterator implements Iterator<Item> {

        @Override
        public boolean hasNext() {
            // TODO
            return false;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        @Override
        public Item next() {
            // TODO
            return null;
        }
    }

    public static void main(String[] args) {

    }
}
