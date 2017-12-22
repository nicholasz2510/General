import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class PercolationStats {
    double[] results;

    public PercolationStats(int n, int trials) {
        results = new double[trials];
        for (int i = 0; i < trials; i++) {
            results[i] = runTrial(n);
        }
    }

    private double runTrial(int n) {
        Percolation percolation = new Percolation(n);
        boolean percolates = false;
        while (!percolates) {
            percolates = percolation.percolates();
        }
    }

    public double mean() {
        return 0.0;
    }

    public double stddev() {
        return 0.0;
    }

    public double confidenceLo() {
        return 0.0;
    }

    public double confidenceHi() {
        return 0.0;
    }

    public static void main(String[] args) {

    }
}
