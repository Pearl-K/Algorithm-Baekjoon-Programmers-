import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int a = n/4;
	
        for (int i = 0; i < a ; i++){
          System.out.printf("long ");
        }
        scan.close();

		System.out.println("int");
	}
}