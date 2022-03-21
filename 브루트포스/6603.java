import java.util.*;

public class Main {
    public static ArrayList<Integer> lotto = new ArrayList<>();
    public static void dfs(int[] s, int idx, int cnt){
        if(cnt == 6){
            for(int x : lotto){
                System.out.print(x+" ");
            }
            System.out.println();
            return;
        }
        int n = s.length;
        if(idx==n) return;
        lotto.add(s[idx]);
        dfs(s, idx+1,cnt+1);
        lotto.remove(lotto.size()-1);
        dfs(s, idx+1,cnt);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            if(n==0) break;
            int[] a = new int[n];
            for(int i = 0; i<n;i++){
                a[i] = sc.nextInt();
            }
            dfs(a, 0,0);
            System.out.println();
        }
    }
}
