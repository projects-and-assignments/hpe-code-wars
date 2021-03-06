import java.util.Scanner;
import java.util.ArrayList;
public class prob15
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String name = "";
        ArrayList<String> normalNames = new ArrayList<String>();
        ArrayList<String> namesWithGems = new ArrayList<String>();
        ArrayList<String> myFinal = new ArrayList<String>();
        ArrayList<String> gems = new ArrayList<String>();
        gems.add("Lapis");
        gems.add("Topaz");
        gems.add("Tourmaline");
        gems.add("Sapphire");
        gems.add("Peridot");
        gems.add("Ruby");
        gems.add("Peal");
        gems.add("Emerald");
        gems.add("Diamond");
        gems.add("Aquamarine");
        gems.add("Amethyst");
        gems.add("Garnet");

        // get input
        while (true) 
        {
            name = in.nextLine();
            if(name.equals("END"))
                break;
            else    
                normalNames.add(name);
        }
        // add names with gem names to a special array
        for(String currName : normalNames)
        {
            for(String gem : gems)
            {
                if(currName.contains(gem))
                {
                    namesWithGems.add(currName);
                    
                }
            }
        }
        // remove the gem named names from the normal array
        for(String gem : gems)
        {
            normalNames.removeIf(s -> s.contains(gem));
        }

        // sort
        normalNames.sort(String::compareToIgnoreCase);
        namesWithGems.sort(String::compareToIgnoreCase);

        myFinal.addAll(namesWithGems);
        myFinal.addAll(normalNames);

        myFinal.forEach(s -> System.out.println(s));
        in.close();
    }
}