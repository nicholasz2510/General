import java.util.Scanner;

public class Interest {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Initial balance: ");
        double bal = in.nextDouble();

        System.out.print("Annual interest rate in percent: ");
        double interest = 1 + ((in.nextDouble() / 12) / 100);

        bal = bal * interest;
        System.out.printf("After first month:     %.2f", bal);
        System.out.println();

        bal = bal * interest;
        System.out.printf("After second month:    %.2f", bal);
        System.out.println();

        bal = bal * interest;
        System.out.printf("After third month:     %.2f", bal);
        System.out.println();
    }
}
