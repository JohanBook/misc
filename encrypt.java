import java.util.Random;
import java.util.Scanner;

// A simple implementation of a shift crypt using a seeded random generator
public class Crypt {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Arguments: [password] [encode/decode] [stdin]");
            return;
        }

        int key = Integer.parseInt(args[0]);
        boolean decrypt = Boolean.parseBoolean(args[1]);

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNext()) {
            System.out.println(crypt(scanner.nextLine(), key, decrypt));
        }

        scanner.close();
    }

    public static String crypt(String in , int seed, boolean decrypt) {
        Random random = new Random(seed);
        String out = "";

        for (char c: in .toCharArray())
            out += (char)(additve(random) * (decrypt ? -1 : 1) + (int) c);

        return out;
    }

    private static int additve(Random random) {
        return 1 + random.nextInt(5) - random.nextInt(5);
    }
}
