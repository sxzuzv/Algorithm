package baekjoon_27433;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(br.readLine());

        System.out.println(factorial(N));
    }

    static long factorial(int n) {
        if(n <= 0) {
            return  1;
        }

        return n * factorial(n-1);
    }
}