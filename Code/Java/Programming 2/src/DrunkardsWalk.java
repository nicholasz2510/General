import java.util.Random;

/**
 * This program simulates a drunkard stumbling through intersections
 */
public class DrunkardsWalk {
    public static void main(String[] args) {
        Random generator = new Random();

        int x = 0;
        int y = 0;

        for (int i = 1; i <= 100; i++) {
            int direction = generator.nextInt(4);
            if (direction == 0) {
                x++;
            }
            if (direction == 1) {
                y++;
            }
            if (direction == 2) {
                x--;
            }
            if (direction == 3) {
                y--;
            }
//            System.out.println("(" + x + ", " + y + ")");
        }

        System.out.println("(" + x + ", " + y + ")");
    }
}
