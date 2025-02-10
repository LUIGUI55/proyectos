import java.util.Scanner;

public class MayorMenor{
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese tres valores numericos:");
        
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        
        int mayor = a;
        int menor = a;
        
        if (b > mayor){
            mayor = b;
        }else if (b < menor){
            menor = b;
        }
        if (c > mayor){
            mayor = c;
        }else if (c < menor){
            menor = c;
        }
        System.out.println("El numero mayor es:" + mayor);
        System.out.println("El numero menor es:" + menor);
    }
}