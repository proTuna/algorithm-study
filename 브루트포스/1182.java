import java.util.*;

public class Main {
    public static int dfs(int[] a,int m, int idx, int sum) {
        if(idx == a.length){
            if(sum == m) {
                return 1;
            }
            else {
                return 0;
            }
        }
        return dfs(a,m,idx+1,sum+a[idx]) + dfs(a,m,idx+1,sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] a = new int[n];
        for(int i = 0;i<n;i++){
            a[i] = sc.nextInt();
        }
        int cnt = dfs(a,s,0,0);
        if(s==0) {
            cnt--;
        }
        System.out.println(cnt);
    }
}