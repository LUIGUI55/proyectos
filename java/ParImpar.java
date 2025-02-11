import java.util.Scanner;

    public class ParImpar{
        public static void main(String [] args){
            
        Scanner scanner = new Scanner(System.in);
    
    
        System.out.println("ingrese un numero:");
        int numero = scanner .nextInt();
        if (numero % 2 == 0 ){
            System.out.println(numero + "el numero es par ");
        }else{
            System.out.println(numero + "Es impar");
        }
        }
    }
    