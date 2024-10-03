import java.io.*;
import java.util.*;

public class Main {
    static int[] mag = new int[4];
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 4; i++) {
            mag[i] = Integer.parseInt(br.readLine(), 2);
        }

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());
            rotate(idx, dir);
        }

        System.out.println(calScore());
    }

    public static boolean sameMag(int a, int b) {
        int bit1 = (mag[a] & (1 << 5)) != 0 ? 1 : 0;
        int bit2 = (mag[b] & (1 << 1)) != 0 ? 1 : 0;
        return bit1 == bit2;
    }

    public static void rotate(int idx, int dir) {
        int rotateD[] = new int[4];
        rotateD[idx] = dir;

        for (int i = idx; i > 0; i--) { // left
            if (sameMag(i-1, i)) break;
            rotateD[i-1] = -rotateD[i];
        }

        for (int i = idx; i < 3; i++) { // right
            if (sameMag(i, i+1)) break;
            rotateD[i+1] = -rotateD[i];
        }
        playRotation(rotateD);
    }

    public static void playRotation(int rotate[]) {
        for (int i = 0; i < 4; i++) {
            if (rotate[i] == 1) {
                CW(i);
            } else if (rotate[i] == -1) {
                CCW(i);
            }
        }
    }

    public static void CW(int idx) {
        if ((mag[idx] & 1) == 1) {
            mag[idx] >>>= 1;
            mag[idx] |= (1 << 7);
        } else mag[idx] >>>= 1;
    }

    public static void CCW(int idx) {
        if ((mag[idx] & (1 << 7)) != 0) {
            mag[idx] <<= 1;
            mag[idx] |= 1;
        } else mag[idx] <<= 1;
    }

    public static int calScore() {
        int ret = 0;
        for (int i = 0; i < 4; i++) {
            ret += (mag[i] & (1 << 7)) == 0 ? 0 : (1 << i);
        }
        return ret;
    }
}