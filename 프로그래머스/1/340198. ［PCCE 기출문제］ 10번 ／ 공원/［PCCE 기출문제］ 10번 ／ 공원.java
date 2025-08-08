import java.util.*;

class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        int parkRow = park.length;
        int parkCol = park[0].length;
        
        mats = Arrays.stream(mats)
             .boxed()
             .sorted(Comparator.reverseOrder())
             .mapToInt(Integer::intValue)
             .toArray();
        
        for (int now: mats) {
            for (int i=0; i<=parkRow-now; i++) {
                for (int j=0; j<=parkCol-now; j++) {
                    boolean tmp = true;
                    
                    for (int x=0; x<now; x++) {
                        for (int y=0; y<now; y++) {
                            if (!park[x+i][y+j].equals("-1")) {
                                tmp = false;
                                break;
                            }
                        }
                    }
                    if (tmp) {
                        answer = now;
                        return answer;
                    }
                }
            }
        }
        return answer;
    }
}