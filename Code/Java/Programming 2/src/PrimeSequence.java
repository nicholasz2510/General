// P10.2

public class PrimeSequence implements Sequence {
    private int n = 2;

    public int next() {
        while (hasFactors(n)) {
            n++;
        }
        n++;
        return n - 1;
    }

    private boolean hasFactors(int num) {
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return true;
            }
        }
        return false;
    }
}
