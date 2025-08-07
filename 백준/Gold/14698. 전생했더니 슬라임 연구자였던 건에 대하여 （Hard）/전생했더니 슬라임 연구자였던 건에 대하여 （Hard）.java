import java.io.*;
import java.util.*;
import java.math.*;

class Main {
    private static final long MOD = 1_000_000_007L;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine().trim());
        
        while(T-- > 0) {
            int N = Integer.parseInt(br.readLine().trim());
            PriorityQueue<BigInteger> pq = new PriorityQueue<>();
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                pq.add(new BigInteger(st.nextToken()));
            }
            
            BigInteger answer = BigInteger.ONE; // 누적 전기 요금
            while(pq.size() > 1) {
                BigInteger one = pq.poll();
                BigInteger two = pq.poll();
                BigInteger cost = one.multiply(two);
                answer = answer.multiply(cost.mod(BigInteger.valueOf(MOD)))
                                .mod(BigInteger.valueOf(MOD));
                pq.add(cost);
            }
            bw.write(answer.mod(BigInteger.valueOf(MOD)).toString());
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();
    }
}