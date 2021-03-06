import java.util.Scanner;
import java.util.ArrayList;
public class prob05
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<String> dates = new ArrayList<String>();
        ArrayList<String> duplicates = new ArrayList<String>();
        for(int i = 0; i < n; i++)
        {
            String currentDate = in.next();
            currentDate = currentDate.substring(0, currentDate.lastIndexOf('/'));
            dates.add(currentDate);
        }
        for(int i = 0; i < dates.size(); i++)
        {
            if(dates.indexOf(dates.get(i)) != dates.lastIndexOf(dates.get(i)))
            {
                // duplicate
                duplicates.add(dates.get(i));
                dates.remove(dates.lastIndexOf(dates.get(i)));
            }
        }
        for(int i = 0; i < dates.size(); i++)
        {
            if(duplicates.indexOf(dates.get(i)) != duplicates.lastIndexOf(dates.get(i)))
            {
                // duplicate
                duplicates.remove(dates.get(i));
            }
        }
        if(duplicates.size() == 0)
        {
            System.out.println(duplicates.size() + "\nduplicates: None");
        }
        else
        {
            System.out.print(duplicates.size() + "\nduplicates: ");
            duplicates.forEach(value -> System.out.print(value + " "));
        }
        in.close();
    }
}