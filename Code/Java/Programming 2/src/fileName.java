public class fileName implements Comparable {
    private String name;
    private int digits;

    public fileName(String aName) {
        int i = aName.length();
        while (i > 0 && Character.isDigit(aName.charAt(i - 1))) {
            i--;
        }
        digits = Integer.parseInt(aName.substring(i));
        name = aName.substring(0, i);
    }

    public String getName() {
        return name;
    }

    public int getDigits() {
        return digits;
    }

    @Override
    public int compareTo(Object obj) {
        fileName other = (fileName) obj;
        int result = this.getName().compareTo(other.getName());
        if (result == 0) {
            return this.getDigits() - other.getDigits();
        }
        return result;
    }
}
