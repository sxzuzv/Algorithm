package baekjoon_10988.loop;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String word;
    static String reverseWord;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        word = br.readLine();
        StringBuilder sb = new StringBuilder();

        for (int i = word.length()-1; i >= 0; i--) {
            sb.append(word.charAt(i));
        }

        reverseWord = sb.toString();

        if(word.equals(reverseWord)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}

