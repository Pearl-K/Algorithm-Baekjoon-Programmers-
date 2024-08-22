import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int R, C, ret;
    static int [] dy = {-1, 0, 1}; // 오른쪽 위, 오른쪽, 오른쪽 아래
    static boolean vst[][];
    static boolean flg;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        int map[][] = new int[R][C];

        for (int i = 0; i < R; i++) {
            String input = br.readLine();
            for (int j = 0; j < C; j++) {
                if (input.charAt(j) == '.') map[i][j] = 0;
                else map[i][j] = 1;
            }
        }

        vst = new boolean[R][C];
        ret = 0;

        for (int i = 0; i < R; i++) {
            flg = false;
            dfs(i, 0, map);
        }

        System.out.println(ret);
    }

    static void dfs(int r, int c, int[][] map) {
        if (c == C - 1) {
            ret++;
            flg = true;
            return;
        }

        for (int i = 0; i < 3; i++) {
            int nr = r + dy[i];
            int nc = c + 1;

            if (0 <= nr && nr < R && !vst[nr][nc] && map[nr][nc] == 0) {
                vst[nr][nc] = true;
                dfs(nr, nc, map);
                if (flg) return;  // 경로를 찾은 경우 즉시 종료
            }
        }
    }
}
