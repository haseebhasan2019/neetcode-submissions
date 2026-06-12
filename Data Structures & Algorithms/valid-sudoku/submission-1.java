class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] set1 = new int[9];
        int[] set2 = new int[9];
        int[] set3 = new int[9];
        int[] rowSet = new int[9];
        for (int i = 0; i < 9; i++) {
            rowSet = new int[9];
            if (i==3 || i==6) {
                set1 = new int[9];
                set2 = new int[9];
                set3 = new int[9];
            }
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                if (j<3) {
                    if (++set1[board[i][j]-'0'-1] > 1) {
                        return false;
                    }
                } else if (j < 6) {
                    if (++set2[board[i][j]-'0'-1] > 1) {
                        return false;
                    }
                } else {
                    if (++set3[board[i][j]-'0'-1] > 1) {
                        return false;
                    }
                }
                if (++rowSet[board[i][j]-'0'-1] > 1) {
                    return false;
                }
            }
            // System.out.println(Arrays.toString(set1));
        }
        for (int i = 0; i < 9; i++) {
            rowSet = new int[9];
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') {
                    continue;
                }
                if (++rowSet[board[j][i]-'0'-1] > 1) {
                    return false;
                }
            }
            System.out.println(Arrays.toString(rowSet));
        }


        return true;
    }
}
/*
Set1 set2 set3 
handle 3 rows at a time
45 sum
*/