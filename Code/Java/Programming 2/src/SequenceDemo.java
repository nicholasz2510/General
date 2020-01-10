public class SequenceDemo {
    public static void main(String[] args) {
        LastDigitDistribution dist1 = new LastDigitDistribution();
        dist1.process(new SquareSequence(), 1000);
        dist1.display();
        System.out.println();

        LastDigitDistribution dist2 = new LastDigitDistribution();
        dist2.process(new RandomSequence(), 1000);
        dist2.display();
        System.out.println();

        LastDigitDistribution dist3 = new LastDigitDistribution();
        dist3.process(new PrimeSequence(), 1000);
        dist3.display();
    }
}
