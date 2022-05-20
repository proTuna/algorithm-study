import java.util.*;
import java.io.*;

public class Main {

    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int t = Integer.parseInt(br.readLine());
        while(t-->0) {
            Queue<Long> pq = new PriorityQueue<>();
            long answer = 0;
            int k = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < k; i++){
                pq.offer(Long.parseLong(st.nextToken()));
            }
            while(true) {
                if(pq.size() == 1) {
                    break;
                }
                long a = pq.poll();
                long b = pq.poll();
                long tmp = a+b;
                answer += tmp;
                pq.add(tmp);
            }
            sb.append(answer+"\n");
        }
        System.out.println(sb.toString());
    }
}
