import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        long st = 1, ed = Long.MAX_VALUE-1;

        while (st < ed) {
            long mid = (st+ed)/2;
            if (canSolve(diffs, times, limit, mid)) {
                ed = mid;
            } else {
                st = mid + 1;
            }
        }
        return (int) st;
    }

    public boolean canSolve(int[] diffs, int[] times, long limit, long level) {
        long curTime = 0;

        for (int i = 0; i < diffs.length; i++) {
            if (diffs[i] <= level) {
                curTime += times[i];
            } else {
                int curCnt = (int)(diffs[i]-level);
                if (i == 0) {
                    curTime += (long) curCnt*times[i] + times[i];
                } else {
                    curTime += (long) curCnt*(times[i]+times[i-1]) + times[i];
                }
            }

            if (curTime > limit) return false;
        }
        return true;
    }
}