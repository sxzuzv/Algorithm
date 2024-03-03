package baekjoon_1913;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/* 1913번 : 달팽이
[문제] 홀수인 자연수 N이 주어지면, 1부터 N^2까지의 자연수를
달팽이 모양으로 N×N의 표에 채울 수 있다.
N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오.
또한 N^2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오.
예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

[입력] 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다.
둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

[출력] N개의 줄에 걸쳐 표를 출력한다.
각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다.
N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

[제한 : 시간 제한 2초]

[예제 입력]
7
35

[예제 출력]
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7
 */

public class Main {
    static int N;   // 자연수 N
    static int target; // 찾아가려는 숫자

    static int[][] snail;   // NxN의 정방행렬

    static BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));

    // '하' -> '우' -> '상' -> '좌' 진행 방향 고정이며, 방향에 따른 좌표 값을 세팅한다.
    static int[] dr = {1, 0, -1, 0};
    static int[] dc = {0, 1, 0, -1};

    // 초기 달팽이의 좌표는 (0,0)이며 '하' 방향을 바라본 상태로 시작한다.
    static int r = 0, c = 0, d = 0;

    // 찾으려는 숫자가 위치한 좌표 값을 초기화한다.
    static int targetR = 0, targetC = 0;

    // StringBuilder 미사용 시, 시간 초과 발생하니 주의!
    static StringBuilder sb = new StringBuilder();

    // 찾으려는 숫자가 위치한 좌표값 찾아서 출력한다.
    static void print(int[][] graph) {
        for (int r = 0; r < graph.length; r++) {
            for (int c = 0; c < graph.length; c++) {
                if (target == snail[r][c]) {
                    targetR = r + 1;
                    targetC = c + 1;
                }
                sb.append(snail[r][c] + " ");
            }
            sb.append("\n");
        }
        sb.append(targetR + " " + targetC);
        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        target = Integer.parseInt(br.readLine());
        snail = new int[N][N];

        for (int i = N*N; i > 0; i--) {
            snail[r][c] = i;

            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N || snail[nr][nc] != 0) {
                d = (d + 1) % 4;
                nr = r + dr[d];
                nc = c + dc[d];
            }

            r = nr;
            c = nc;
        }
        print(snail);
    }
}
