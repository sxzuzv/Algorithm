package baekjoon_2559;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/* 2559번 : 수열
[문제] 매일 측정한 온도가 정수의 수열로 주어졌을 때,
연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

[입력] 첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다.
첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다. N은 2 이상 100,000 이하이다.
두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다.
둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다.
이 수들은 모두 -100 이상 100 이하이다.

[출력]
첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.

[예제 입력]
10 2
3 -2 -4 -9 0 3 7 13 8 -3

[예제 출력]
21
 */

public class Main {
    static BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
    static int maxTemp; // 온도의 합이 최대가 되는 값
    static int N, K;    // 배열 원소 개수 N, 구간 합 내 원소 개수 K(연속적인 K일)

    public static void main(String[] args) throws IOException {
        // 배열 원소 개수와 구간합 내 원소 개수를 저장한다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 입력 받은 온도 수열(문자열)을 정수형 배열로 만든다.
        int[] temperatures = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();

        int acc = 0; // 초기 구간 합 저장 변수

        // 가장 처음의 구간 합을 구하고 최대 구간 합으로 지정한다.
        for (int i = 0; i < K; i++) {
            acc += temperatures[i];
        }
        maxTemp = acc;

        // 구간을 변경하며 최대 구간 합을 구한다.
        for (int i = 0; i < N-K; i++) {
            // 슬라이딩 윈도우
            // 한 칸씩 윈도우를 밀기 때문에 원소의 중복 값이 발생한다.
            // 좌측 원소는 제거하고, 우측 원소는 더하여 새로운 구간 합을 구한다.
            // '기존 구간 합 - 좌측 원소 값 + 우측 원소 값'
            acc = acc - temperatures[i] + temperatures[i+K];

            // max() 메서드를 활용해 큰 값을 비교하여 최대 구간 합을 저장한다.
            maxTemp = Math.max(maxTemp, acc);
        }

        System.out.println(maxTemp);
    }
}
