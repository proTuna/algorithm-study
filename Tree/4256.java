import java.util.*;
import java.io.*;

public class Main {

    public static int[] preorder;
    public static int[] inorder;
    public static StringBuilder sb = new StringBuilder();

    public static void dfs(int root, int s, int e){
        for(int i=s; i<e;i++){
            if(inorder[i] == preorder[root]){
                dfs(root+1,s,i);
                dfs(root+i+1-s,i+1,e);
                sb.append(preorder[root]+" ");
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            int n = Integer.parseInt(br.readLine());
            preorder = new int[n];
            inorder = new int[n];
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i<n;i++){
                preorder[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i<n;i++){
                inorder[i] = Integer.parseInt(st.nextToken());
            }
            dfs(0,0,n);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
