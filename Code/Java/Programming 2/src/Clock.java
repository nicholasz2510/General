public class Clock {
    private int alarmHours = 24;
    private int alarmMinutes = 60;

    public void setAlarm(int hours, int minutes) {
        alarmHours = hours;
        alarmMinutes = minutes;
    }

    public String getHours() {
        return java.time.LocalTime.now().toString().substring(0, 2);
    }

    public String getMinutes() {
        return java.time.LocalTime.now().toString().substring(3, 5);
    }

    public String getTime() {
        int currHours = Integer.parseInt(getHours());
        int currMinutes = Integer.parseInt(getMinutes());

        if ((currHours == alarmHours && currMinutes >= alarmMinutes) || (currHours > alarmHours)) {
            alarmHours = 24;
            alarmMinutes = 60;
            return currHours + ":" + getMinutes() + " Alarm";
        }

        return currHours + ":" + currMinutes;
    }

    public static void main(String[] args) {
        WorldClock c = new WorldClock(0);

        System.out.println(c.getHours());
        System.out.println(c.getMinutes());
        c.setAlarm(0, 0);
        System.out.println(c.getTime());
        System.out.println(c.getTime());
    }
}
