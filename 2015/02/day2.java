import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class day2 {

    public static void main(String[] args) throws Exception {
        String[] inputData = readInput();
        System.out.println(part1(inputData));
        System.out.println(part2(inputData));
    }

    private static int part1(String[] inputData) throws Exception {
        int total = 0;
        List<Integer> area = new ArrayList<>(List.of(0,0,0));
        List<Integer> dims = new ArrayList<>();

        for(int i = 0; i < inputData.length; i++) {
            dims = Arrays.stream(inputData[i].split("x"))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
            
            area.set(0, dims.get(0) * dims.get(1));
            area.set(1, dims.get(1) * dims.get(2));
            area.set(2, dims.get(2) * dims.get(0));

            total += 2 * (area.get(0) + area.get(1) + area.get(2)) + Collections.min(area);
        }

        return total;
    }

    private static int part2(String[] inputData) throws Exception {
        int total = 0;
        List<Integer> per = new ArrayList<>(List.of(0,0,0));
        List<Integer> dims = new ArrayList<>();

        for(int i = 0; i < inputData.length; i++) {
            dims = Arrays.stream(inputData[i].split("x"))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

            per.set(0, 2 * (dims.get(0) + dims.get(1)));
            per.set(1, 2 * (dims.get(1) + dims.get(2)));
            per.set(2, 2 * (dims.get(2) + dims.get(0)));

            total += Collections.min(per) + dims.get(0) * dims.get(1) * dims.get(2);
        }

        return total;
    }

    private static String[] readInput() throws Exception {
        List<String> lines = Collections.emptyList();
        lines = Files.readAllLines(Paths.get("./input.txt"), StandardCharsets.UTF_8);

        return lines.toArray(new String[lines.size()]);
    }
}