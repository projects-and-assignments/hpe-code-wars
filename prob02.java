import java.util.Scanner;
public class prob02
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        double h = in.nextDouble();
        double r = in.nextDouble();

        double V = Math.PI * r * r * h;
        System.out.printf("%.2f cubic inches", V);
        
        in.close();
    }
}