import java.util.HashMap;
import java.util.Objects;
import java.nio.file.Files;
import java.nio.file.Paths;

public class day3 {

    public static class Coords {
        private int x;
        private int y;
        private int hashCode;

        public Coords(int x, int y) {
            this.x = x;
            this.y = y;
            this.hashCode = Objects.hash(x, y);
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public void move(char direction) {
            if(direction == '^') this.y += 1;
            else if(direction == 'v') this.y -= 1;
            else if(direction == '>') this.x += 1;
            else if(direction == '<') this.x -= 1;

            this.hashCode = Objects.hash(x, y);
        }

        @Override
        public boolean equals(Object o) {
            if(this == o) return true;
            if(o == null || getClass() != o.getClass()) return false;

            Coords that = (Coords) o;
            return x == that.x && y == that.y;
        }

        @Override
        public int hashCode() {
            return this.hashCode;
        }

        @Override
        public String toString()
        {
            return "(" + this.getX() + "," + this.getY() + ")";
        }
    }

    public static void main(String[] args) throws Exception {
        String inputData = readInput();
        System.out.println(part1(inputData));
        System.out.println(part2(inputData));
    }

    private static int part1(String inputData) throws Exception {
        HashMap<String, Integer> map = new HashMap<>();
        Coords currPos = new Coords(0,0);

        map.put(currPos.toString(), 1);

        for(int i = 0; i < inputData.length(); i++) {
            currPos.move(inputData.charAt(i));
            String key = currPos.toString();

            if(map.containsKey(key)) {
                map.put(key, map.get(key) + 1);
            }
            else {
                map.put(key, 1);
            }
        }

        return map.size();
    }

    private static int part2(String inputData) throws Exception {
        HashMap<String, Integer> map = new HashMap<>();
        Coords santaPos = new Coords(0,0);
        Coords robotPos = new Coords(0,0);
        boolean santaTurn = true;

        map.put(santaPos.toString(), 2);

        for(int i = 0; i < inputData.length(); i++) {
            if(santaTurn) {
                santaPos.move(inputData.charAt(i));
                String key = santaPos.toString();

                if(map.containsKey(key)) {
                    map.put(key, map.get(key) + 1);
                }
                else {
                    map.put(key, 1);
                }
            }
            else {
                robotPos.move(inputData.charAt(i));
                String key = robotPos.toString();

                if(map.containsKey(key)) {
                    map.put(key, map.get(key) + 1);
                }
                else {
                    map.put(key, 1);
                }
            }

            santaTurn = !santaTurn;
        }

        return map.size();
    }

    private static String readInput() throws Exception {
        String data = "";
        data = new String(Files.readAllBytes(Paths.get("./input.txt")));
        return data;
    }
}
