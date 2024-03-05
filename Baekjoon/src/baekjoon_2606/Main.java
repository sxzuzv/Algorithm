package baekjoon_2606;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

/* 2606번 : 바이러스
[문제] 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

[입력] 첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서
직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

[출력] 1번 컴퓨터가 웜 바이러스에 걸렸을 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

[제한 : 시간 제한 1초]

[예제 입력]
7
6
1 2
2 3
1 5
5 2
5 6
4 7

[예제 출력]
4
 */

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int cnt, V, E; // 정답, 노드갯수, 간선갯수
    static HashSet<Integer> visited = new HashSet<>(); // 방문체크 갯수
    static ArrayDeque<Integer> stack = new ArrayDeque<>(Arrays.asList(1)); // 스택
    static int[][] adj;

    public static void main(String[] args) throws IOException {
        V = Integer.parseInt(br.readLine());
        E = Integer.parseInt(br.readLine());
        adj = new int[V+1][V+1];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            adj[start][end] = adj[end][start] = 1; // 양방향 그래프
        }

        while (!stack.isEmpty()) {
            int cur = stack.removeLast();

            if (!visited.contains(cur)) {
                // HashSet에 방문 노드를 기록한다.
                visited.add(cur);
            }

            for (int nxt = 0; nxt < V + 1; nxt++) {
                if (!visited.contains(nxt) && adj[cur][nxt] == 1) {
                    stack.add(nxt);
                }
            }
        }
        System.out.println(visited.size()-1);
    }
}
