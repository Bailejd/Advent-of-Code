// Day 1: Not Quite Lisp
//
// Results
// Part 1: 74
// Part 2: 1795

import java.nio.file.Files;
import java.nio.file.Paths;

public class day1 {

    public static void main(String[] args) throws Exception {
        String inputData = readInput();
        System.out.println(part1(inputData));
        System.out.println(part2(inputData));
    }

    private static int part1(String inputData) throws Exception {
        int floor = 0;

        for(int i = 0; i < inputData.length(); i++) {
            if(inputData.charAt(i) == '(') floor += 1;
            else if(inputData.charAt(i) == ')') floor -= 1;
        }

        return floor;
    }

    private static int part2(String inputData) throws Exception {
        int floor = 0;

        for(int i = 0; i < inputData.length(); i++) {
            if(inputData.charAt(i) == '(') floor += 1;
            else if(inputData.charAt(i) == ')') floor -= 1;

            if(floor < 0) return i+1;
        }

        return -1;
    }

    private static String readInput() throws Exception {
        String data = "";
        data = new String(Files.readAllBytes(Paths.get("./input.txt")));
        return data;
    }
}