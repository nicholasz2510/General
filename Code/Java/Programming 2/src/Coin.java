import java.io.FileNotFoundException;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Coin {
    private int value;
    private String name;

    public Coin(int aValue, String aName) {
        value = aValue;
        name = aName;
    }

    public Coin() {

    }

    public int getValue() {
        return value;
    }

    public void read(Scanner in) throws FileNotFoundException {
        name = in.next();
        System.out.println(name);
        try {
            value = in.nextInt();
            System.out.println(value);
        } catch (InputMismatchException exception) {
            System.out.println(exception);
        }
    }
}
