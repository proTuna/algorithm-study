import java.util.*;

public class Main {
    public static int n,m;
    public static int[] dx = {-1,0,1,0};
    public static int[] dy = {0,1,0,-1};
    public static char[][] board;
    public static int go(int step, int x1, int y1, int x2, int y2){
        if(step==11) return -1;
        boolean c1 = false;
        boolean c2 = false;
        if(x1<0 || x1>=n || y1<0 || y1>=m) c1 = true;
        if(x2<0 || x2>=n || y2<0 || y2>=m) c2 = true;
        if(c1 && c2) return -1;
        if(c1 || c2) return step;
        int ans = -1;
        for(int k = 0; k<4; k++) {
            int nx1 = x1+dx[k];
            int ny1 = y1+dy[k];
            int nx2 = x2+dx[k];
            int ny2 = y2+dy[k];
            if(0<=nx1&& nx1<n && 0<=ny1 && ny1<m && board[nx1][ny1] == '#') {
                nx1=x1;
                ny1=y1;
            }
            if(0<=nx2&& nx2<n && 0<=ny2 && ny2<m && board[nx2][ny2] == '#') {
                nx2=x2;
                ny2=y2;
            }
            int tmp = go(step+1, nx1,ny1,nx2,ny2);
            if(tmp == -1) continue;
            if(ans==-1 || ans>tmp){
                ans = tmp;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        board = new char[n][m];
        int x1,y1,x2,y2;
        x1=y1=x2=y2=-1;
        for (int i=0; i<n; i++) {
            board[i] = sc.next().toCharArray();
            for (int j=0; j<m; j++) {
                if (board[i][j] == 'o') {
                    if (x1 == -1) {
                        x1 = i;
                        y1 = j;
                    } else {
                        x2 = i;
                        y2 = j;
                    }
                    board[i][j] = '.';
                }
            }
        }
        System.out.println(go(0,x1,y1,x2,y2));
    }
}