public class ChessBoard{
    String[][] board = new String[8][8];

    public void startPosition(){
        for(int i = 0; i<8; i++) {
            for(int j = 0; j<8; j++){
                // first fill with empty String
                board[i][j] = " ";
            }
        }
        // rook
        board[0][0] = "BR";
        board[0][7] = "BR";
        board[7][0] = "WR";
        board[7][7] = "WR";
        // horse
        board[0][1] = "BH";
        board[0][6] = "BH";
        board[7][1] = "WH";
        board[7][6] = "WH";
        // bishops
        board[0][2] = "BB";
        board[0][5] = "BB";
        board[7][2] = "WB";
        board[7][5] = "WB";
        // queen
        board[0][3] = "BQ";
        board[7][3] = "WQ";
        // king
        board[0][4] = "BK";
        board[7][4] = "WK";
        //pawns
        board[1][0] = "BP";
        board[1][1] = "BP";
        board[1][2] = "BP";
        board[1][3] = "BP";
        board[1][4] = "BP";
        board[1][5] = "BP";
        board[1][6] = "BP";
        board[1][7] = "BP";
        board[6][0] = "WP";
        board[6][1] = "WP";
        board[6][2] = "WP";
        board[6][3] = "WP";
        board[6][4] = "WP";
        board[6][5] = "WP";
        board[6][6] = "WP";
        board[6][7] = "WP";
    }

    public void printBoard() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args){
        ChessBoard board = new ChessBoard();
        board.startPosition();
        board.printBoard();
    }

}