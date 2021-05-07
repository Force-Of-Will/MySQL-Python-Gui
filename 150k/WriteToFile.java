import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors
import java.util.*;

public class WriteToFile {

public static void playerstxt(int n){
   try{
   FileWriter myWriter = new FileWriter("Players.txt");
   String[] pos = new String[] {"QB", "RB", "WR"};//3long
   String[] team = new String[] {"Aggies", "Lobos", "Vultures", "Cougars", "Hawks"};//5long
   
   for(int i = 0; i < n; i++){
      int x = (int) (Math.random() * 3);      
      int x1 = (int) (Math.random() * 5);
      int touchdowns = (int) (Math.random() * 50);
      int yards = (int) (Math.random() * 1000);
      int salary = (int) (Math.random() * 50000);
      myWriter.write("Player" + (i+1) + "," + i + "," + team[x1] + "," + pos[x] + "," + touchdowns + "," + yards +"," + salary + "\n");
   }//end for
   myWriter.close();
   } catch (IOException e){
      System.out.println("An error occured");
      e.printStackTrace();
   }
   
}

public static void playtxt(int n){
   try{
   FileWriter myWriter = new FileWriter("Play.txt");
   for(int i = 0; i < n; i++){
      myWriter.write(i + "," + (n-i-1) + "\n");
   }//end for
   myWriter.close();
   } catch (IOException e){
      System.out.println("An error occured");
      e.printStackTrace();
   }
   
}




public static void gametxt(int n){
   try{
   FileWriter myWriter = new FileWriter("Game.txt");
   String[] res = new String[] {"W", "L", "T"};//3long
   String[] stadium = new String[] {"Aggie Stadium", "Lobo Stadium", "Vulture Stadium", "Cougar Stadium", "Hawk Stadium"};//5long
   
   for(int i = 0; i < n; i++){
      int x = (int) (Math.random() * 3);      
      int x1 = (int) (Math.random() * 5);
      int month = ((int) (Math.random() * 12)) + 1;
      int day = ((int) (Math.random() * 28)) + 1;
      int year = ((int) (Math.random() * 50)) + 1950;
      int attendance = (int) (Math.random() * 10000);
      int rev = (int) (Math.random() * 100000);
      myWriter.write(i +"," + year + "/" + month + "/" + day +"," + stadium[x1] + "," + res[x] + "," + attendance + "," + rev + "\n");
   }//end for
   myWriter.close();
   } catch (IOException e){
      System.out.println("An error occured");
      e.printStackTrace();
   }
   
}


public static void main(String[] args) {
   playerstxt(150000);
   playtxt(150000);
   gametxt(150000);
  
}
}