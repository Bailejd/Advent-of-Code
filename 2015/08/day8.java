// Day 8: Matchsticks
//
// Results
// Part 1: 1333
// Part 2: 2046

import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class day8 {
    
    public static void main(String[] args) throws Exception {
        String[] data = readInput();

        System.out.println(part1(data));
        System.out.println(part2(data));
    }

    public static int part1(String[] data) {
        int totalCharMem = 0;
        int totalCharCode = 0;

        for(int i = 0; i < data.length; i++) {
            char[] charArray = data[i].substring(1, data[i].length()-1).toCharArray();
            int charMem = 0;
            int charCode = data[i].length();
            boolean firstEscape = true;

            for(int j = 0; j < charArray.length; j++) {
                if(charArray[j] == '\\' && firstEscape) {
                    firstEscape = false;
                    if(charArray[j+1] == 'x') {
                        // charMem -= 2;
                        j += 2;
                    }
                    continue;
                }
                charMem++;
                firstEscape = true;
            }

            totalCharMem += charMem;
            totalCharCode += charCode;
        }

        return totalCharCode - totalCharMem;
    }

    public static int part2(String[] data) {
        int totalCharsNew = 0;
        int totalCharsOriginal = 0;

        for(int i = 0; i < data.length; i++) {
            ArrayList<Character> newString = new ArrayList<Character>();

            newString.add('"');

            for(int j = 0; j < data[i].length(); j++) {
                char curr = data[i].charAt(j);
                if(curr == '"') {
                    newString.add('\\');
                    newString.add('"');
                }
                else if(curr == '\\') {
                    newString.add('\\');
                    newString.add('\\');
                }
                else {
                    newString.add(curr);
                }
            }

            newString.add('"');

            totalCharsNew += newString.size();
            totalCharsOriginal += data[i].length();
        }

        return totalCharsNew - totalCharsOriginal;
    }

    public static String[] readInput() throws Exception {
        List<String> lines = Collections.emptyList();
        lines = Files.readAllLines(Paths.get("./input.txt"), StandardCharsets.UTF_8);

        return lines.toArray(new String[lines.size()]);
    }
}
