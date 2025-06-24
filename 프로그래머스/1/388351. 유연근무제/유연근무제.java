class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        final int WEEK_RANGE = 7;
        int ans = 0;
        int n = schedules.length;

        // 1) 주말 인덱스
        int satIdx = (6 - startday + 7) % 7;
        int sunIdx = (satIdx + 1) % 7;
        boolean[] isWeekend = new boolean[WEEK_RANGE];
        isWeekend[satIdx] = isWeekend[sunIdx] = true;

        // 2) 직원별 ‘평일 10분 전 도착’ 판정
        for (int i = 0; i < n; i++) {
            int goalMinutes = toMinute(schedules[i]) + 10;
            boolean onTimeAllWeek = true;

            for (int d = 0; d < WEEK_RANGE; d++) {
                if (isWeekend[d]) continue;

                int nowMinutes = toMinute(timelogs[i][d]);
                
                if (nowMinutes > goalMinutes) {
                    onTimeAllWeek = false; 
                    break;
                }
            }
            if (onTimeAllWeek) ans++;
        }
        return ans;
    }

    private int toMinute(int hhmm) {
        return (hhmm / 100) * 60 + (hhmm % 100);
    }
}