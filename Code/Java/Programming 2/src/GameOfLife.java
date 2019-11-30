public class GameOfLife {
    private static char[][] currGen = {
            { ' ', ' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', ' ' , ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', ' ' , ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', 'o' , ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
            { ' ', 'o', 'o', 'o', ' ', ' ', 'o' , 'o', ' ', 'o', 'o', ' ', ' ', 'o', 'o', 'o', ' ' },
            { ' ', ' ', ' ', 'o', ' ', 'o', ' ' , 'o', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', 'o' , ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', 'o' , ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', 'o', ' ', 'o', ' ' , 'o', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ', ' ' },
            { ' ', 'o', 'o', 'o', ' ', ' ', 'o' , 'o', ' ', 'o', 'o', ' ', ' ', 'o', 'o', 'o', ' ' },
            { ' ', ' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', 'o' , ' ', ' ', ' ', 'o', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', ' ' , ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', 'o', ' ' , ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ' },
            { ' ', ' ', ' ', ' ', ' ', ' ', ' ' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' }
    };

    private static void nextGen() {
        char[][] nextGen = new char[currGen.length][];
        for (int i = 0; i < currGen.length; i++) {
            nextGen[i] = currGen[i].clone();
        }

        for (int y = 0; y < currGen.length; y++){
            for (int x = 0; x < currGen[0].length; x++) {
                if (currGen[y][x] == ' ' && numNeighbors(x, y) == 3) {
                    nextGen[y][x] = 'o';
                } if (currGen[y][x] == 'o' && (numNeighbors(x, y) <= 1 || numNeighbors(x, y) >= 4)) {
                    nextGen[y][x] = ' ';
                }
            }
        }

        for (int i = 0; i < nextGen.length; i++) {
            currGen[i] = nextGen[i].clone();
        }
    }

    private static void pause() {
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            System.err.format("IOException: %s%n", e);
        }
    }

    private static int numNeighbors(int x, int y) {
        int num = 0;

        for (int xDir = -1; xDir <= 1; xDir++) {
            for (int yDir = -1; yDir <= 1; yDir++) {
                int checkX = x + xDir;
                int checkY = y + yDir;
                if ((checkX >= 0 && checkX < currGen[0].length) && (checkY >= 0 && checkY < currGen.length)) {
                    if (currGen[y][x] == 'o') {
                        num++;
                    }
                }
            }
        }

//        if (y > 0) {
//            if (x > 0) {
//                if (currGen[y - 1][x - 1] == 'o') {
//                    num++;
//                }
//            }
//            if (currGen[y - 1][x] == 'o') {
//                num++;
//            }
//            if (x < currGen[0].length - 1) {
//                if (currGen[y - 1][x + 1] == 'o') {
//                    num++;
//                }
//            }
//        } if (x > 0) {
//            if (currGen[y][x - 1] == 'o') {
//                num++;
//            }
//        } if (x < currGen[0].length - 1) {
//            if (currGen[y][x + 1] == 'o') {
//                num++;
//            }
//        } if (y < currGen.length - 1) {
//            if (x > 0) {
//                if (currGen[y + 1][x - 1] == 'o') {
//                    num++;
//                }
//            } if (currGen[y + 1][x] == 'o') {
//                num++;
//            } if (x < currGen[0].length - 1) {
//                if (currGen[y + 1][x + 1] == 'o') {
//                    num++;
//                }
//            }
//        }

        return num;
    }

    public static void main(String[] args) {
        int currGenNum = 0;

        while (true) {
            pause();

            for (char[] row : currGen) {
                for (char c : row) {
                    System.out.print(" " + c);
                }
                System.out.println();
            }
            System.out.println("Generation " + currGenNum);

            currGenNum++;
            nextGen();
        }
    }
}
