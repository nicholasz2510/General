import java.util.ArrayList;
import java.util.Stack;

public class stackPermutations {
    public static ArrayList<String> permutations(String s) {
        ArrayList<String> result = new ArrayList<String>();
        Stack<String> stack = new Stack<>();

        stack.push("+" + s);
        while (!stack.empty()) {
            String top = stack.pop();
            if (top.substring(top.length() - 1).equals("+")) {
                result.add(top.substring(0, top.length() - 1));
            } else {
                int plusPlace = top.indexOf('+');
                for (int i = 1; i < (top.length() - plusPlace); i++) {
                    String toPush = top.substring(0, plusPlace + i) + top.substring(plusPlace + i + 1);
                    int newPlusPlace = toPush.indexOf('+') - 1;
                    toPush = toPush.substring(0, newPlusPlace + 1) + top.substring(plusPlace + i, plusPlace + i + 1) + toPush.substring(newPlusPlace + 1);
                    stack.push(toPush);
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(permutations("meat"));
    }
}
