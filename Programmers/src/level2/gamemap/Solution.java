package level2.gamemap;

import java.util.ArrayDeque;

/* 게임 맵 최단거리


 */

class Solution {
    static ArrayDeque<int[]> Q;
    static int N, M; // 행, 열 크기 1, 1인 경우는 주어지지 않음.
    static int[][] dist; // 방문 체크 2차원 배열
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, -1 ,1};
    static int[][] board;
    static int answer;
    static boolean flag = false;

    static void bfs() {
        Q = new ArrayDeque<>();
        Q.addLast(new int[] {0, 0}); // 맨 처음 점은 0, 0 입니다. (문제에선 1, 1)
        dist[0][0] = 1;

        while (!Q.isEmpty()) {
            int[] current = Q.removeFirst();
            int cur_r = current[0];
            int cur_c = current[1];

            if (cur_r == N-1 && cur_c == M-1) { // 해당 위치를 찾은 경우는?
                flag = true; // 찾았다고 체크하고
                return;
            }

            for (int j = 0; j < 4; j++) {
                int nr = cur_r + dr[j];
                int nc = cur_c + dc[j];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                    continue; // 맵 밖이면 안되고
                }

                if (board[nr][nc] == 0 || dist[nr][nc] > 0) {
                    continue; // 벽이거나 이미 방문했으면 안되고
                }
                dist[nr][nc] = dist[cur_r][cur_c] + 1;
                Q.addLast(new int[] {nr, nc});
            }
        }
    }

    static int solution(int[][] maps) {
        board = maps;
        N = maps.length; // 행 갯수
        M = maps[0].length; // 열 갯수
        dist = new int[N][M]; // 모두 false로 초기화
        bfs(); // bfs를 돌립니다!
        answer = flag ? dist[N-1][M-1] : -1;
        return answer;
    }
}