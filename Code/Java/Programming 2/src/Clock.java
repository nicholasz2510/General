public class Clock {
    public String getHours() {
        return java.time.LocalTime.now().toString().substring(0, 2);
    }

    public String getMinutes() {
        return java.time.LocalTime.now().toString().substring(3, 5);
    }

    public String getTime() {
        return getHours() + ":" + getMinutes();
    }

    public static void main(String[] args) {
        Clock c = new Clock();

        System.out.println(c.getHours());
        System.out.println(c.getMinutes());
        System.out.println(c.getTime());
    }
}
