import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] rq;
    private int head;
    private int tail;
    private int size;
    private int capacity;

    /**
     * The constructor
     */
    public RandomizedQueue() {
        capacity = 2;
        rq = (Item[]) new Object[capacity];
        head = 0;
        tail = 0;
        size = 0;
    }

    /**
     * Checks whether or not the queue is empty
     * @return whether or not the queue is empty
     */
    public boolean isEmpty() {
        if (size == 0) {
            assert (head == tail) && (rq[head] == null) && (rq[tail] == null);
        } else {
            assert ((head == tail) && (rq[head] != null) && (rq[tail] != null)) || (head != tail);
        }
        return size == 0;
    }

    /**
     * finds the size
     * @return the size of the queue
     */
    public int size() {
        return size;
    }

    /**
     * adds an item to the queue
     * @param item is the item you are adding
     */
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException("Sorry, but we do not support adding null to the queue");
        }
        int indexOfItem;
        if (!isEmpty()) {
            indexOfItem = (StdRandom.uniform(size) + head) % capacity;
            rq[tail] = rq[indexOfItem];
        } else {
            indexOfItem = head;
        }
        rq[indexOfItem] = item;
        tail = (tail + 1) % capacity;
        size++;
        if (head == tail) {
            resize();
        }
    }

    private void resize() {
        assert capacity >= size;
        int oldCapacity = capacity;
        capacity = capacity * 2;
        Item[] resized = (Item[]) new Object[capacity];
        int s = head;
        for (int i = 0; i < size; i++) {
            resized[i] = rq[s];
            s = (s + 1) % oldCapacity;
        }
        head = 0;
        tail = size;
        rq = resized;
    }

    /**
     * removes a random item
     * @return the item which was removed
     */
    public Item dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Sorry, but the queue is currently empty");
        }
        Item item = rq[head];
        rq[head] = null;
        head = (head + 1) % capacity;
        size--;
        return item;
    }

    /**
     * gives a random item in the queue
     * @return a random item
     */
    public Item sample() {
        if (isEmpty()) {
            throw new NoSuchElementException("Sorry, but the queue is currently empty");
        }
        return rq[(StdRandom.uniform(size) + head) % capacity];
    }

    /**
     * gives you a new iterator
     * @return a new instance of the ListIterator
     */
    @Override
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private int current = 0;
        private final Item[] shuffled;

        public RandomizedQueueIterator() {
            shuffled = (Item[]) new Object[size];
            int curr = head;
            for (int i = 0; i < size; i++) {
                shuffled[i] = rq[curr];
                curr = (curr + 1) % capacity;
            }
            StdRandom.shuffle(shuffled);
        }

        @Override
        public boolean hasNext() {
            return current < size;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

        @Override
        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException("Sorry, but you have reached the end of the queue");
            }
            int c = current;
            current++;
            return shuffled[c];
        }
    }
}
