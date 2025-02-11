import java.util.Scanner;

public class OrdenarNumericos{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("ingrese el primer numero :");
        int numero1 = scanner .nextInt();
        
        System.out.println("Ingrese el segundo numero:");
        int numero2 = scanner .nextInt();
        
        int temporal ;
        if (numero1 > numero2){
            temporal = numero1;
            temporal = numero2;
            numero2 = temporal;
        }
         
        System.out.println("Los numeros ordenados de menor a mayor son");
        System.out.println(numero1 + numero2);
        
    }
}
