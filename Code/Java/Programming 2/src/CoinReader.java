import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class CoinReader {
    public static ArrayList<Coin> readFile(String filename) throws IOException {
        File inFile = new File(filename);
        ArrayList<Coin> list = new ArrayList<>();
        try (Scanner in = new Scanner(inFile)) {
            while (in.hasNextLine()) {
                Coin coin = new Coin();
                coin.read(in);
                list.add(coin);
            }
        }
        return list;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Coin> coins = null;

        boolean read = false;
        while (!read) {
            try {
                System.out.print("Please enter the file name: ");
                String filename = in.next();

                coins = readFile(filename);
                read = true;
            } catch (IOException exception) {
                System.out.println(exception);
            }
        }
        in.close();
        System.out.println(coins);
        int sum = 0;
        for (Coin c : coins) {
            sum += c.getValue();
        }
        System.out.println(sum);
    }
}
