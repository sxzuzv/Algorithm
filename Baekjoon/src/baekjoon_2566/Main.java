package baekjoon_2566;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* 2566번 : 최댓값
[문제] 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고
그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

[입력] 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다.
주어지는 수는 100보다 작은 자연수 또는 0이다.

[출력] 첫째 줄에 최댓값을 출력하고,
둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

[제한 : 시간 제한 1초]

[예제 입력]
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80

[예제 출력]
90
5 7
 */

public class Main {
    static int[][] matrix = new int[9][9];
    static int max, num;
    static int maxR, maxC;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        StringTokenizer st;

        for (int r = 0; r < 9; r++) {
            st = new StringTokenizer(br.readLine());

            // 9x9 행렬을 만들지 않아도 문제 풀이가 가능함을 이용한다.
            // 행렬을 만드는 작업 없이, 입력 받은 숫자들로 최댓값을 가려낸다.
            for (int c = 0; c < 9; c++) {
                num = Integer.parseInt(st.nextToken());

                if (max < num) {
                    max = num;
                    maxR = r;
                    maxC = c;
                }

            }
        }

        System.out.println(max);
        System.out.printf("%d %d", maxR+1, maxC+1);
    }
}
