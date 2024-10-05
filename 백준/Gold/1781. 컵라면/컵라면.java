import java.util.*;
import java.io.*;

public class Main {

    static int N;
    static long ret;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        PriorityQueue<Pair> pq = new PriorityQueue<>((p1, p2) -> {
            if(p1.cnt == p2.cnt){
                return Integer.compare(p2.date, p1.date);
            }
            else{
                return Integer.compare(p2.cnt, p1.cnt);
            }
        });

        StringTokenizer st = null;
        Pair items[] = new Pair[N];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            items[i] = new Pair(d, c);
        }

        Arrays.sort(items, new Comparator<Pair>() {
            @Override
            public int compare(Pair o1, Pair o2) {
                if(o1.date < o2.date) return 1;
                else if(o1.date == o2.date) return 0;
                else return -1;
            }
        });

        int retCnt = 0;
        int retSum = 0;
        for(int i = 200000; i>= 1; i--){
            while(retCnt < items.length && items[retCnt].date == i){
                pq.add(items[retCnt++]);
            }
            if(pq.isEmpty()) continue;
            retSum += pq.poll().cnt;
        }
        System.out.println(retSum);
    }

    public static class Pair{
        int date;
        int cnt;

        public Pair(int x, int y){
            this.date = x;
            this.cnt = y;
        }
    }
}