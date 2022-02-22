// Day 6: Probably a Fire Hazard
//
// Results
// Part 1: 400410
// Part 2: 15343601

import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;

public class day6 {
    
    // Part 1
    public static class Lights {
        private int[][] grid;
        private int numOn;

        public Lights(int m, int n) {
            this.grid = new int[m][n];
            this.numOn = 0;
        }

        public void toggle(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    if(this.grid[i][j] == 0) {
                        this.grid[i][j] = 1;
                        this.numOn += 1;
                    }
                    else {
                        this.grid[i][j] = 0;
                        this.numOn -= 1;
                    }
                }
            }
        }

        public void off(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    if(this.grid[i][j] == 1) {
                        this.grid[i][j] = 0;
                        this.numOn -= 1;
                    }
                }
            }
        }

        public void on(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    if(this.grid[i][j] == 0) {
                        this.grid[i][j] = 1;
                        this.numOn += 1;
                    }
                }
            }
        }

        public int getNumOn() {
            return this.numOn;
        }
    }

    // Part 2
    public static class FancyLights {
        private int[][] grid;
        private int totalBrightness;

        public FancyLights(int m, int n) {
            this.grid = new int[m][n];
            this.totalBrightness = 0;
        }

        // Toggle actually adds 2 brightness levels
        public void toggle(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    this.grid[i][j] += 2;
                    this.totalBrightness += 2;
                }
            }
        }

        // Off actually subtracts 1 brightness level to a minimum of 0
        public void off(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    if(this.grid[i][j] != 0) {
                        this.grid[i][j] -= 1;
                        this.totalBrightness -= 1;
                    }
                }
            }
        }

        // On actually adds 1 brightness level
        public void on(int startx, int starty, int endx, int endy) {
            for(int i = startx; i <= endx; i++) {
                for(int j = starty; j <= endy; j++) {
                    this.grid[i][j] += 1;
                    this.totalBrightness += 1;
                }
            }
        }

        public int getTotalBrightness() {
            return this.totalBrightness;
        }
    }

    public static void main(String[] args) throws Exception {
        String[] data = readInput();
        
        System.out.println(part1(data));
        System.out.println(part2(data));
    }

    public static int part1(String[] data) {
        Lights obj = new Lights(1000,1000);

        for(int i = 0; i < data.length; i++) {
            String[] temp = data[i].split(" ");

            if(temp[0].equals("turn")) {
                String[] start = temp[2].split(",");
                String[] end = temp[4].split(",");
                
                if(temp[1].equals("on")) {
                    obj.on(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
                }
                else {
                    obj.off(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
                }
            }
            else if(temp[0].equals("toggle")) {
                String[] start = temp[1].split(",");
                String[] end = temp[3].split(",");

                obj.toggle(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
            }
        }

        return obj.getNumOn();
    }

    // Part 2
    // On now means increase brightness level by 1
    // Off now means decrease brightness level by 1 to a minimum of 0
    // Toggle now means increase brightness level by 2
    public static int part2(String[] data) {
        FancyLights obj = new FancyLights(1000,1000);

        for(int i = 0; i < data.length; i++) {
            String[] temp = data[i].split(" ");

            if(temp[0].equals("turn")) {
                String[] start = temp[2].split(",");
                String[] end = temp[4].split(",");
                
                if(temp[1].equals("on")) {
                    obj.on(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
                }
                else {
                    obj.off(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
                }
            }
            else if(temp[0].equals("toggle")) {
                String[] start = temp[1].split(",");
                String[] end = temp[3].split(",");

                obj.toggle(Integer.parseInt(start[0]), Integer.parseInt(start[1]), Integer.parseInt(end[0]), Integer.parseInt(end[1]));
            }
        }

        return obj.getTotalBrightness();
    }

    public static String[] readInput() throws Exception {
        List<String> lines = Collections.emptyList();
        lines = Files.readAllLines(Paths.get("./input.txt"), StandardCharsets.UTF_8);

        return lines.toArray(new String[lines.size()]);
    }
}
