class Solution {
    public int solution(int[] stones, int k) {
        int left = 1, right = 200_000_000, ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canCross(stones, k, mid)) {
                ans = mid;
                left = mid+1;
            } else {
                right = mid-1; 
            }
        }
        return ans;
    }

    // mid명(people)이 건널 수 있는지 판정
    private boolean canCross(int[] stones, int k, int people) {
        int zeroCount = 0;
        for (int s : stones) {
            // 사람이 people명 지나갔다고 가정했을 때 남은 내구도
            if (s < people) {
                if (++zeroCount >= k) {
                    // 연속으로 k개 이상 못 밟을 디딤돌이 나오면 실패
                    return false;
                }
            } else {
                // 내구도 충분한 돌을 밟으면 연속 카운터 리셋
                zeroCount = 0;
            }
        }
        return true;
    }
}