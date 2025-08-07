import java.io.*;
import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = {};
        int num = name.length;
        Map<String, Integer> scoreMap = new HashMap<>();
        
        for (int i=0; i<num; i++) {
            scoreMap.put(name[i], yearning[i]);
        }
        
        int photoNum = photo.length;
        int retScore[] = new int[photoNum];
        for (int i=0; i<photoNum; i++) {
            int tmp = 0;
            for (String now: photo[i]) {
                tmp += scoreMap.getOrDefault(now, 0);
            }
            retScore[i] = tmp;
        }
        answer = retScore;
        return answer;
    }
}