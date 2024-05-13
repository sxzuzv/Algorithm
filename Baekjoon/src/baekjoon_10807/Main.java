package baekjoon_10807;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 10807번: 개수 세기
 * [문제] 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
 * 
 * [입력] 첫째 줄에 정수의 개수 N(1<=N<=100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어 있다.
 * 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다는 크거나 같으며, 100보다 작거나 같다.
 * 
 * [출력] 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
 */

public class Main {
    // BufferedReader 선언: 한 문장 단위로 입력 받는다. (Enter 기준)
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // StringTokenizer 선언: BufferedReader로 입력 받은 한 문장을 공백 기준으로 문자 단위로 분리한다.
    static StringTokenizer st;
    static int N, v;    // 정수 개수 N, 찾으려고 하는 정수 v

    public static void main(String[] args) throws IOException {
        int count = 0; // 찾아야 하는 정수 개수 카운트

        // 첫 줄에 들어온 정수 개수 N
        N = Integer.parseInt(br.readLine());

        int[] nums = new int[N];
        
        // 두 번째 줄에 들어오는 정수 배열 값
        // 1) BufferedReader를 사용하여 한 문장을 받는다.
        // 2) 받은 한 문장을 StringTokenizer를 이용해 공백 기준으로 문자 단위로 나눈다.
        st = new StringTokenizer(br.readLine());

        // 나눈 문자를 정수형으로 파싱하여 배열에 넣는다.
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 세 번째 줄에 들어오는 찾아야 하는 정수 v
        v = Integer.parseInt(br.readLine());

        // 배열에 찾아야 하는 정수 v가 몇 개 있는지 카운트한다.
        for (int i = 0; i < N; i++) {
            if (nums[i] == v) {
                count++;
            }
        }

        System.out.println(count);
    }
}