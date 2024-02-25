package baekjoon_10988.twopointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String word;
    static String reverseWord;
    static int answer = 1;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        word = br.readLine();

        for(int i = 0; i <= (word.length() - 1) / 2; i++) {
            if(word.charAt(i) != word.charAt(word.length()-1-i)) {
                answer = 0;
                break;
            }
        }

        System.out.println(answer);
    }
}