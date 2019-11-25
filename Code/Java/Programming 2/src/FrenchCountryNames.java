import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * This program reads the French name of a country and adds the correct article
 */
public class FrenchCountryNames {
    public static void main(String[] args) {

        String[] mascExceptionsArray = {"Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"};
        List<String> mascExceptions = Arrays.asList(mascExceptionsArray);

        Scanner in = new Scanner(System.in);
        System.out.print("Country name: ");
        if (in.hasNext()) {
            String country = in.next();
            if (country.equals("Etats-Unis") || country.equals("Pays-Bas")) {
                System.out.println("les " + country);
            } else if (mascExceptions.contains(country)) {
                System.out.println("le " + country);
            } else if ("AEIOUaeiou".contains(Character.toString(country.charAt(0)))) {
                System.out.println("l'" + country);
            } else if (country.charAt(country.length() - 1) == 'e') {
                System.out.println("la " + country);
            } else {
                System.out.println("le " + country);
            }
        }
    }
}
