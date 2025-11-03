import java.util.*;

class Solution {
    private int n;
    private int[][] q;
    private int[] ans;
    private int answer;
    
    private void comb(int start, List<Integer> current) {
        if (current.size() == 5){
            if (validate(current)) answer++;
            return;
        }
        
        for (int i=start; i<=n; i++) {
            current.add(i);
            comb(i+1, current);
            current.remove(current.size()-1);
        }
    }
    
    private boolean validate(List<Integer> combination) {
        Set<Integer> nums = new HashSet<>(combination);
        
        for (int i = 0; i < q.length; i++) {
            int count = 0;
            for (int num : q[i]) if (nums.contains(num)) count++;
            if (count != ans[i]) return false;
        }
        return true;
    }
    
    public int solution(int n, int[][] q, int[] ans) {
        this.n = n;
        this.q = q;
        this.ans = ans;
        answer = 0;
        comb(1, new ArrayList<Integer>());
        return answer;
    }
}