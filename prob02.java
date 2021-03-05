import java.util.Scanner;
public class prob02
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        long c = in.nextLong();
        long p = in.nextLong();
        System.out.println(c*p);
        in.close();
    }
}