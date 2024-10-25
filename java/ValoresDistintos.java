import java.util.Scanner;

public class ValoresDistintos{
    public static void main(String [] args){
        Scanner scanner  = new Scanner(System.in);
        
        System.out.println("ingrese dos valores distintos");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        if (a == b){
            System.out.println("Los valores son iguales");
        }else if  (a > b){
            System.out.println(a + "es el numero mayor");
        }else{
            System.out.println(b + "Es el numero mayor");
        }
    }
}