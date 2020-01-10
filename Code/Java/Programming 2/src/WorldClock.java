public class WorldClock extends Clock {
    private int timeOffset;

    public WorldClock(int offset) {
        timeOffset = offset;
    }

    public void setAlarm(int hours, int minutes) {
        super.setAlarm(hours + timeOffset, minutes + timeOffset);
    }

    public String getHours() {
        return String.format("%02d", Integer.parseInt(java.time.LocalTime.now().toString().substring(0, 2)) + timeOffset);
    }

    public String getMinutes() {
        return String.format("%02d", Integer.parseInt(java.time.LocalTime.now().toString().substring(3, 5)) + timeOffset);
    }
}
