package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

/* 인접 행렬 & 인접 리스트 생성 */

public class Main {
    /* 노드 개수 7개, 간선 개수 8개
    7 8
    1 2
    1 3
    2 4
    2 5
    4 6
    5 6
    6 7
    3 7
     */

    static BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
    static int[][] arr;
    static int V;
    static int E;


    public static void main(String[] args) throws IOException {
        array();
        list();
    }

    public static void array() throws IOException {
        System.out.println("===== 인접행렬 =====");
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        // 노트 개수가 V개이고, 0부터 시작하는 노드는 없다고 한다면?
        // V+1로 arr 크기를 지정한다.
        arr = new int[V+1][V+1];

        // 간선의 개수만큼 반복한다.
        // 왜냐하면, 그만큼 노드가 연결돼 있다는 것이고
        // 연결 정보에 대해서 arr에 표기를 해주어야 하기 때문!
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            // 1과 2가 연결됐다고 하면, 1은 start이고 2는 end가 된다.
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt((st.nextToken()));

            // 양방향 그래프임을 고려하여, start와 end가 반대가 되는 값에도 1(true) 체크!
            arr[start][end] = 1;
            arr[end][start] = 1;
        }
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }

    /* 인접행렬 -> 인접리스트 */
    static ArrayList[] list; // 2차원 인접리스트
    public static void list() throws IOException {
        System.out.println("===== 인접리스트 =====");
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        // 인덱스를 고려하여 +1로 list 크기를 설정한다.
        list = new ArrayList[V+1];

        for (int i = 0; i < V + 1; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());

            // 1과 2가 연결돼 있다면 start는 1, end는 2
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt((st.nextToken()));

            // 인접리스트로 변경하면서 행은 고정이지만 열은 가변적이게 된다.
            // 인접행렬에서 1(true) 체크된 것들을 기준으로 인접리스트로 변경한다.
            // 인접행렬에서 1행에 <2, 3>이 true
            // 인접행렬에서 2행에 <1, 4, 5>가 true
            // 이 경우 (1,2) 및 (2,1)이 되는 것이므로 반대가 되는 값에도 1(true) 체크!
            list[start].add(end);
            list[end].add(start);
        }
        System.out.println(Arrays.toString(list));
    }
}