import java.io.*;
import java.util.*;

public class Main {
	
	static int K, W, H;
	static int grid[][];
	static int path[][][];
	
	static int dr[] = {-1, 1, 0, 0};
	static int dc[] = {0, 0, -1, 1};
	
	// 나이트처럼 3칸 이동 (총 8가지)
    static final int[] knightR = {2, 2, -2, -2, 1, 1, -1, -1};
    static final int[] knightC = {1, -1, 1, -1, 2, -2, 2, -2};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		
		grid = new int[H][W]; // 세로, 가로 순서 조심
		path = new int[H][W][K+1]; // K번 이동 만큼 3차원 배열 제작, K번까지 이동이므로 K+1 인덱스 주의
		
		for(int i=0; i<H; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<W; j++) grid[i][j] = Integer.parseInt(st.nextToken());
		}
		
		System.out.println(bfs(0, 0, K));
	}
	
	static int bfs(int sr, int sc, int cnt) {
		
		Queue<int []> Q = new LinkedList<>();
		Q.add(new int[] {sr, sc, cnt});
		
		while(!Q.isEmpty()) {
			int cur[] = Q.poll();
			
			int curR = cur[0];
			int curC = cur[1];
			int cntLeft = cur[2];
			
			if (curR == H-1 && curC == W-1) return path[curR][curC][cntLeft];
			
			for(int i=0; i<4; i++) {
				int nr = curR + dr[i];
				int nc = curC + dc[i];
				
				if(0 <= nr && nr < H && 0 <= nc && nc < W && grid[nr][nc] == 0 && path[nr][nc][cntLeft] == 0) {
					// 다음으로 이동 가능한 경우 (한 칸)
					path[nr][nc][cntLeft] = path[curR][curC][cntLeft] + 1;
					Q.add(new int[] {nr, nc, cntLeft});
				}
			}
			
			for(int i=0; i<8; i++) {
				int nr = curR + knightR[i];
				int nc = curC + knightC[i];
				
				if(0 <= nr && nr < H && 0 <= nc && nc < W && grid[nr][nc] == 0 &&  cntLeft > 0 && path[nr][nc][cntLeft-1] == 0) {
					// 다음으로 이동 가능한 경우 (나이트 처럼 이동, 이동 카운트 하나 깎기)
					path[nr][nc][cntLeft-1] = path[curR][curC][cntLeft] + 1;
					Q.add(new int[] {nr, nc, cntLeft-1});
				}
			}
		}
		return -1; //도달할 수 없는 경우
	}
}