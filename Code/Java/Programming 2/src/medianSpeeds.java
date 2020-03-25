import java.util.*;

public class medianSpeeds {
    private static int[] arr;

    public static int select(int k, int a, int b) {
        int p = arr[a];
        int n1 = partition(a, b, p) - a;
        int n2 = 1;
        int n3 = b - (n1 + n2 + a);
        if (k < n1) {
            return select(k, a, a + n1);
        } else if (k > n1 + n2) {
            return select(k - (n1 + n2), a + n1 + n2, b);
        }
        return p;
    }

    public static int partition(int a, int b, int p) {
        int i = a;
        int j = b + 1;
        while (i < j) {
            i++;
            while (arr[i] < p) { i++; }
            j--;
            while (arr[j] > p) { j--; }
            if (i < j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[a];
        arr[a] = arr[j];
        arr[j] = temp;
        return j;
    }

    public static void main(String[] args) {
        Random rd = new Random();
        arr = new int[11];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i;
        } for (int i = 0; i < arr.length; i++) {
            int newIndex = rd.nextInt(arr.length);
            int temp = arr[i];
            arr[i] = arr[newIndex];
            arr[newIndex] = temp;
        }

        System.out.println(select(arr.length / 2, 0, arr.length - 1));
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
