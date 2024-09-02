import java.io.*;
import java.util.*;

public class Main {
    
    static int N;
    static int[][] grid;
    static boolean[] visited;
    static long minCost = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        grid = new int[N][N];
        
        for(int i=0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        for(int i=0; i < N; i++) {
            visited = new boolean[N];
            visited[i] = true;
            tsp(i, i, 0, 0);
        }
        
        System.out.println(minCost);
    }
    
    static void tsp(int start, int current, int count, int cost) {
    	
        // 모든 정점을 다 방문했을 경우
        if(count == N-1) {
            // 마지막 정점에서 시작 정점으로 돌아가는 비용을 더해 최소 비용 구하기
        	if (grid[current][start] > 0) {
        		cost += grid[current][start];
                minCost = Math.min(minCost, cost);
                return;
        	}
        }

        for(int next = 0; next < N; next++) {
            if(!visited[next] && grid[current][next] > 0) { 
            	// 방문하지 않은 정점 탐색
                visited[next] = true;
                tsp(start, next, count + 1, cost + grid[current][next]);
                visited[next] = false; // 다음 순열을 위해 방문 기록 초기화
            }
        }
    }
}