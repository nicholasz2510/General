import java.util.Scanner;

public class ZipCodeConverter {
    private static String zipToBar(int zipCode) {
        return "a";
//        TODO
    }

    private int barToZip(String barCode) {
        return 0;
//        TODO
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            System.out.print("1) ZIP code -> bar code 2) Bar code -> ZIP code (1/2) ");
            int decision = in.nextInt();
            if (decision == 1) {
                boolean validInput = false;
                int zipCode = 0;
                while (!validInput) {
                    System.out.print("What is the ZIP code you would like to convert? ");
                    zipCode = in.nextInt();
                    if (!(Integer.toString(zipCode).length() == 5)) {
                        System.out.println("The ZIP code has to be 5 digits. ");
                        validInput = false;
                    } else {
                        validInput = true;
                    }
                }

                System.out.println(zipToBar(zipCode));
            } else if (decision == 2) {
                //            TODO
            }
        }
    }
}
