package baekjoon_11659;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/* 11659번 : 구간 합 구하기 4
[문제] 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

[입력] 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
둘째 줄에는 N개의 수가 주어진다.
수는 1,000보다 작거나 같은 자연수이다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

[출력]
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

[제한 : 시간 제한 1초]
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

[예제 입력]
5 3
5 4 3 2 1
1 3
2 4
5 5

[예제 출력]
12
9
1
 */

public class Main {
    // BufferedReaader 선언 : Enter를 기준으로 구분 (한 문장 단위로 받는다.)
    // 버퍼 공간에 저장해두었다가 한 번에 내보낸다. (속도 UP)
    // 입력 받은 값을 나눠줘야 하므로 코드가 길어지는 단점이 존재한다.
    static BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));

    // StringTokenizer 선언
    // BufferedReader를 통해 입력 받은 한 문장을 공백 기준으로 문자 단위로 분리한다.
    static StringTokenizer st;

    static int N, M; // 배열 원소 개수 N, 구간 합을 구해야 하는 횟수 M

    static int[] nums;

    // BufferedReader 사용 시, main 함수에서 IOException 처리 필수!
    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 Enter까지의 한 문장을 받는다.
        // 한 줄에 들어온 문자열을 StringTokenizer를 이용해 공백 기준으로 나눈다.
        // 배열 원소 개수(N)와 구간 합 구하는 횟수(M)가 공백 구분으로 입력된다.
        st = new StringTokenizer(br.readLine());

        // 공백 기준으로 나눈 문자 중 처음 들어온 문자(배열 원소 개수)를 저장한다.
        // 문자 형태이므로 정수형으로 변환한다.
        N = Integer.parseInt(st.nextToken());

        // 공백 기준으로 나눈 문자 중 두 번째로 들어온 문자(구간 합 구하는 횟수)를 저장한다.
        // 문자 형태이므로 정수형으로 변환한다.
        M = Integer.parseInt(st.nextToken());

        // 한 줄로 입력 받은 문자열을 정수형 배열로 만든다.
        // 1) 입력 받은 문자열 한 줄을 공백 기준으로 나눠 문자열 배열을 만든다.
        // 2) 배열 속 문자열을 정수로 변환한다. => mapToInt(Integer:parseInt)
        // 3) toArray() 메서드를 사용하여 최종적으로 정수형 배열을 만든다.
        nums = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();

        // 배열에 대한 누적 합 배열을 생성한다.
        // nums = [5, 4, 3, 2, 1]일 경우,
        // 누적 합 배열 nums = [5, 9, 12, 14, 15]
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }

        //
        for (int i = 0; i < M; i++) {
            // 입력 받은 값으로 i번 째 수와 j번 째 수를 지정한다.
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            // 특정 구간에 해당되는 구간합을 구한다.
            System.out.println(nums[end-1] - (start == 1? 0 : nums[start-2]));
        }
    }
}
