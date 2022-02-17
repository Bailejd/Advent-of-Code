// Day 5: Doesn't He Have Intern-Elves For This?
//
// Results
// Part 1: 236
// Part 2:

import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class day5 {

    public static class NiceString {
        private String string;
        private boolean isNice;
        private boolean containsDouble;
        private boolean containsInvalid;
        private int numVowels;

        public NiceString(String s) {
            this.string = s;
            this.isNice = false;
            this.containsDouble = false;
            this.containsInvalid = false;
            this.numVowels = 0;

            checkNice(string);
        }

        private void checkNice(String s) {
            String last = "-";
            String vowels = "aeiou";
            List<String> invalid = Arrays.asList("ab", "cd", "pq", "xy");

            for(int i = 0; i < s.length(); i++) {
                String curr = String.valueOf(s.charAt(i));

                if(vowels.contains(curr)) {
                    this.numVowels += 1;
                }

                if(last != "-") {
                    if(last.equals(curr)) {
                        this.containsDouble = true;
                    }
                    if(invalid.contains(last + curr)) {
                        this.containsInvalid = true;
                    }
                }

                last = curr;
            }

            if(containsInvalid) this.isNice = false;
            else if(numVowels >= 3 && containsDouble) this.isNice = true;
        }

        public boolean getIsNice() {
            return this.isNice;
        }
    }

    public static void main(String[] args) throws Exception {
        String[] inputData = readInput();
        System.out.println(part1(inputData));
        System.out.println(part2(inputData));
    }

    private static int part1(String[] inputData) throws Exception {
        int total = 0;

        for(int i = 0; i < inputData.length; i++) {
            if(new NiceString(inputData[i]).getIsNice()) total += 1;
        }

        return total;
    }

    private static int part2(String[] inputData) throws Exception {
        int total = 0;

        return total;
    }

    private static String[] readInput() throws Exception {
        List<String> lines = Collections.emptyList();
        lines = Files.readAllLines(Paths.get("./input.txt"), StandardCharsets.UTF_8);

        return lines.toArray(new String[lines.size()]);
    }
}