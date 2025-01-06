import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++){
            int N = Integer.parseInt(br.readLine());
            int Wcnt = 0;
            int Bcnt = 0;

            String Now = br.readLine();
            String Goal = br.readLine();

            for (int j = 0; j < N; j++){
                if(Now.charAt(j) != Goal.charAt(j)) {
                    if(Now.charAt(j) == 'W') Wcnt++;
                    else Bcnt++;
                }
            }
            int res = Math.min(Wcnt, Bcnt) + Math.abs(Wcnt-Bcnt);
            System.out.println(res);
        }
    }
}