/**
 * Name: Nicholas Zhang
 * Date: 12/24/2017
 * Purpose: This implements union find for percolation.
 */

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private final int n; // the length of one side of the grid which you are trying to make percolate.
    private boolean[] openedSites; // tells if the site is opened with the ID as the index
    private int numOpened = 0; // is the number of already opened sites
    private final WeightedQuickUnionUF percolatesUf; // this is the union-find we use for checking if it percolates
    private final WeightedQuickUnionUF fullUf; // this only checks if a site is full

    /**
     * This is the constructor.
     *
     * @param n is the length of one side of the grid which you are trying to make percolate.
     */
    public Percolation(int n) {
        if (n <= 0) {
            throw new java.lang.IllegalArgumentException();
        }
        int gridSize = (n + 1) * (n + 1);
        openedSites = new boolean[gridSize];
        for (int i = 0; i < gridSize; i++) {
            openedSites[i] = false;
        }
        this.n = n;
        percolatesUf = new WeightedQuickUnionUF(gridSize);
        fullUf = new WeightedQuickUnionUF(gridSize);
        for (int i = 1; i <= n; i++) {
            percolatesUf.union(xyTo1D(1, i), 0);
            fullUf.union(xyTo1D(1, i), 0);
            percolatesUf.union(xyTo1D(n, i), 1);
        }
    }

    /**
     * This opens up a site by connecting it to its adjacent (left, right, up, and down) already opened sites
     *
     * @param row
     * @param col
     */
    public void open(int row, int col) {
        if (row < 1 || col < 1 || row > n || col > n) {
            throw new java.lang.IllegalArgumentException();
        }
        if (validateIndices(row, col)) {
            if (!isOpen(row, col)) {
                openedSites[xyTo1D(row, col)] = true;
                numOpened++;
            }
            if (validateIndices(col - 1, row) && isOpen(row, col - 1)) {
                percolatesUf.union(xyTo1D(row, col), xyTo1D(row, col - 1));
                fullUf.union(xyTo1D(row, col), xyTo1D(row, col - 1));
            }
            if (validateIndices(col + 1, row) && isOpen(row, col + 1)) {
                percolatesUf.union(xyTo1D(row, col), xyTo1D(row, col + 1));
                fullUf.union(xyTo1D(row, col), xyTo1D(row, col + 1));
            }
            if (validateIndices(col, row - 1) && isOpen(row - 1, col)) {
                percolatesUf.union(xyTo1D(row, col), xyTo1D(row - 1, col));
                fullUf.union(xyTo1D(row, col), xyTo1D(row - 1, col));
            }
            if (validateIndices(col, row + 1) && isOpen(row + 1, col)) {
                percolatesUf.union(xyTo1D(row, col), xyTo1D(row + 1, col));
                fullUf.union(xyTo1D(row, col), xyTo1D(row + 1, col));
            }
        }
    }

    /**
     * Checks if the given site is opened
     *
     * @param row
     * @param col
     * @return
     */
    public boolean isOpen(int row, int col) {
        if (row < 1 || col < 1 || row > n || col > n) {
            throw new java.lang.IllegalArgumentException();
        }
        return openedSites[xyTo1D(row, col)];
    }

    /**
     * Checks if the given site is full
     *
     * @param row
     * @param col
     * @return
     */
    public boolean isFull(int row, int col) {
        if (row < 1 || col < 1 || row > n || col > n) {
            throw new java.lang.IllegalArgumentException();
        }
        return fullUf.connected(xyTo1D(row, col), 0) && isOpen(row, col);
    }

    /**
     * Finds the total number of sites you have already opened
     *
     * @return
     */
    public int numberOfOpenSites() {
        return numOpened;
    }

    /**
     * Checks if the system lets water flow through
     *
     * @return
     */
    public boolean percolates() {
        if (n == 1 && numOpened == 0) {
            return false;
        }
        return percolatesUf.connected(0, 1);
    }

    /**
     * With a given row and col with a site, finds the ID at that site
     *
     * @param row
     * @param col
     * @return
     */
    private int xyTo1D(int row, int col) {
        return col + row * n;
    }

    /**
     * checks that the site is a real site in the group of sites
     *
     * @param col
     * @param row
     * @return
     */
    private boolean validateIndices(int col, int row) {
        return (1 <= col && col <= n) && (1 <= row && row <= n);
    }
}
