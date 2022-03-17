// Day 10: Elves Look, Elves Say
//
// Results
// Part 1: 492982
// Part 2: 6989950

import java.nio.file.Files;
import java.nio.file.Paths;

public class day10 {
    
    public static void main(String[] args) throws Exception {
        String data = readInput();

        // Part 1
        System.out.println(lookAndSay(data, 40));

        // Part 2
        System.out.println(lookAndSay(data, 50));
    }

    public static int lookAndSay(String data, int steps) {
        String input = data;

        for(int i = 0; i < steps; i++) {
            StringBuilder new_string = new StringBuilder();

            for(int j = 0; j < input.length(); j++) {
                int count = 1;
                char ch = input.charAt(j);

                while (j + 1 < input.length() && input.charAt(j + 1) == ch) {
                    j++;
                    count++;
                }

                new_string.append(count);
                new_string.append(ch);
            }

            input = new_string.toString();
        }

        return input.length();
    }

    public static String readInput() throws Exception {
        String data = "";
        data = new String(Files.readAllBytes(Paths.get("./input.txt")));
        return data; 
    }
}
