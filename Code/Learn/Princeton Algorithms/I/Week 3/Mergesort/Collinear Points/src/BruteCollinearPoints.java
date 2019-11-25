import java.util.ArrayList;
import java.util.Arrays;

public class BruteCollinearPoints {
    private ArrayList<LineSegment> segments;
    private int nOfSegments;

    public BruteCollinearPoints(Point[] points) {
        if (points == null) {
            throw new IllegalArgumentException();
        }
        if (hasDuplicates(points)) {
            throw new IllegalArgumentException();
        }
        for (Point p : points) {
            if (p == null) {
                throw new IllegalArgumentException();
            }
        }

        nOfSegments = 0;
        Point[] currentFour = new Point[4];
        segments = new ArrayList<>();

        for (Point p : points) {
            for (Point q : points) {
                for (Point r : points) {
                    for (Point s : points) {
                        if (isValidTuple(p, q, r, s)) {
                            if (p.slopeTo(q) == p.slopeTo(r) && p.slopeTo(r) == p.slopeTo(s)) {
                                segments.add(new LineSegment(p, s));
                                nOfSegments++;
                            }
                        }
                    }
                }
            }
        }
    }

    private boolean hasDuplicates(Point[] a) {
        Point[] copy = Arrays.copyOf(a, a.length);
        Arrays.sort(copy);
        int j = 1;
        for (int i = 0; i <= copy.length - 2; i++) {
            if (copy[i] == copy[j]) {
                return true;
            }
        }
        return false;
    }
    
    private boolean isValidTuple(Point p, Point q, Point r, Point s) {
        Point[] currentFour = new Point[4];
        currentFour[0] = p;
        currentFour[1] = q;
        currentFour[2] = r;
        currentFour[3] = s;
        if (hasDuplicates(currentFour)) {
            return false;
        }
        Point[] tempFour = Arrays.copyOf(currentFour, currentFour.length);
        Arrays.sort(currentFour);
        if (tempFour != currentFour) {
            return false;
        }
        return true;
    }

    public int numberOfSegments() {
        return nOfSegments;
    }

    public LineSegment[] segments() {
        return segments.toArray(new LineSegment[segments.size()]);
    }
}
