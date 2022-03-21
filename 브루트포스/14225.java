import java.util.*;

public class Main {
    public static boolean[] c = new boolean[20*100000+10];
    public static int[] a = new int[20];
    public static int n;
    public static void dfs(int idx, int sum){
        if(idx==n){
            c[sum] = true;
            return;
        }
        dfs(idx+1, sum+a[idx]);
        dfs(idx+1,sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for(int i = 0; i<n;i++) {
            a[i] = sc.nextInt();
        }
        dfs(0,0);
        for(int i = 1;; i++) {
            if(c[i] == false){
                System.out.println(i);
                break;
            }
        }
    }
}
