import java.util.Scanner;

public class ZipCodeConverter {
    private static final String[] ENCODING = {"||:::", ":::||", "::|:|", "::||:", ":|::|", ":|:|:", ":||::", "|:::|", "|::|:", "|:|::"};

    private static String zipToBar(int zipCode) {
        String barcode = "|";
        int total = 0;
        for (char c : Integer.toString(zipCode).toCharArray()) {
            int curr = Character.getNumericValue(c);
            barcode += ENCODING[curr];
            total += curr;
        }
        barcode += ENCODING[((int) (Math.ceil(total / 10.0) * 10)) - total] + "|";

        return barcode;
    }

    private static int barToZip(String barcode) {
        String zipCode = "";
        int total = 0;
        for (int i = 1; i < barcode.length() - 6; i += 5) {
            int digit = digitToInt(barcode.substring(i, i + 5));
            zipCode += digit;
            total += digit;
        }

        int checkDigit = digitToInt(barcode.substring(barcode.length() - 6, barcode.length() - 1));
        if (((total + checkDigit) % 10) != 0) {
            System.out.println("There was an error with the check digit. ");
        }

        return Integer.parseInt(zipCode);
    }

    private static int digitToInt(String digit) {
        for (int x = 0; x < ENCODING.length; x++) {
            if (ENCODING[x].equals(digit)) {
                return x;
            }
        }
        System.out.println("There was an error in the input. ");
        return -1;
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
                System.out.println();
            } else if (decision == 2) {
                boolean validInput = false;
                String barcode = "";
                while (!validInput) {
                    System.out.print("What is the barcode you would like to convert? ");
                    barcode = in.next();
                    if (!(barcode.length() == 32)) {
                        System.out.println("The barcode has to be 32 characters. ");
                        validInput = false;
                    } else {
                        validInput = true;
                    }
                }

                System.out.println(barToZip(barcode));
                System.out.println();
            } else {
                System.out.println("Please enter either 1 or 2. ");
            }
        }
    }
}
