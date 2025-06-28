import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int F = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int G = Integer.parseInt(st.nextToken());
        int U = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        int result = solve(F, S, G, U, D);

        if (result == -1) {
            System.out.println("use the stairs");
        } else {
            System.out.println(result);
        }
    }

    private static int solve(int F, int S, int G, int U, int D) {
        boolean[] visited = new boolean[F+1];
        int[] dist = new int[F+1];
        Queue<Integer> q = new LinkedList<>();
        visited[S] = true;
        dist[S] = 0;
        q.add(S);

        while (!q.isEmpty()) {
            int curr = q.poll();
            if (curr == G) return dist[curr];

            for (int go : new int[]{U, -D}) {
                int next = curr + go;
                if (next >= 1 && next <= F && !visited[next]) {
                    visited[next] = true;
                    dist[next] = dist[curr] + 1;
                    q.add(next);
                }
            }
        }
        return -1;
    }

    private static boolean isValidRange(int F, int N) {
        return (1 <= N) && (N <= F);
    }
}