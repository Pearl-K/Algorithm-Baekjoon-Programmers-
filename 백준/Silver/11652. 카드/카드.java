import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static Long maxNum;
    static int ret = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        HashMap<Long, Integer> cnt = new HashMap<>();

        for(int i=0; i<N; i++){
            long num = Long.parseLong(br.readLine());
            cnt.put(num, cnt.getOrDefault(num, 0)+1);
            if(cnt.get(num) > ret){
                maxNum = num;
                ret = cnt.get(num);
            } else if(cnt.get(num).equals(ret)){
                maxNum = Math.min(maxNum, num);
            }
        }
        System.out.println(maxNum);
    }
}