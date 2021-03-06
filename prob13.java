public class prob13 
{
    public static void main(String[] args) 
    {
        java.util.Scanner in = new java.util.Scanner(System.in);
        String vehicle = in.next();
        int ramp1 = in.nextInt();
        double rate1 = in.nextDouble();
        double riverWidth = in.nextDouble();

        double time1 = Math.sqrt((2*ramp1)/rate1);
        double speed1 = time1 * rate1;
        double distance = (speed1 * speed1)/9.805;
        
        String base = vehicle + " will reach a speed of " + String.format("%.2f", speed1) + " m/s on a " + ramp1 + " meter ramp, crossing " + String.format("%.1f", distance) + " of " + riverWidth + " meters";
        if(distance < riverWidth-5)
            System.out.println(base + ", SPLASH!");
        else if(distance >= riverWidth -5 && distance <= riverWidth)
            System.out.println(base + ", BARELY MADE IT!");
        else if(distance > riverWidth)
            System.out.println(base + ", LIKE A BOSS!");
    }
}   