import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private static final double CONFIDENCE_95 = 1.96;
    private final double[] results;
    private final double mean;
    private final double stddev;

    /**
     * this is the constructor, it is also where we run the trials
     * @param n is one side
     * @param trials
     */
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new java.lang.IllegalArgumentException();
        }
        results = new double[trials];
        for (int t = 0; t < trials; t++) {
            results[t] = runTrial(n);
        }
        mean = StdStats.mean(results);
        stddev = StdStats.stddev(results);
    }

    /**
     * this runs a single trial
     * @param n is one side
     * @return
     */
    private double runTrial(int n) {
        boolean percolated = false;
        Percolation p = new Percolation(n);
        while (!percolated) {
            p.open(StdRandom.uniform(1, n + 1), StdRandom.uniform(1, n + 1));
            if (p.percolates()) {
                percolated = true;
            }
        }
        return ((double) p.numberOfOpenSites()) / (n * n);
    }

    /**
     * finds the mean of all the results
     * @return
     */
    public double mean() {
        return mean;
    }

    /**
     * finds the standard deviation of the results, if there was only one trial it will simply return Double.NaN
     * @return
     */
    public double stddev() {
        if (results.length == 1) {
            return Double.NaN;
        }
        return stddev;
    }

    /**
     * finds the low part of the confidence interval for the percolation threshold
     * @return
     */
    public double confidenceLo() {
        return mean() - (CONFIDENCE_95 * stddev()) / Math.sqrt(results.length);
    }

    /**
     * finds the low part of the confidence interval for the percolation threshold
     * @return
     */
    public double confidenceHi() {
        return mean() + (CONFIDENCE_95 * stddev()) / Math.sqrt(results.length);
    }

    /**
     * takes command line arguments n and T (for length of one side and number of trials) and outputs the mean,
     * standard deviation, and 95% confidence interval from the results
     * @param args
     */
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int t = Integer.parseInt(args[1]);
        PercolationStats stats = new PercolationStats(n, t);
        System.out.println("mean                    = " + stats.mean());
        System.out.println("stddev                  = " + stats.stddev());
        System.out.println("95% confidence interval = [" + stats.confidenceLo() + ", " + stats.confidenceHi() + "]");
    }
}
