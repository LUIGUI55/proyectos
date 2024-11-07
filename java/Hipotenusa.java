import java.util.Scanner;

public class Hipotenusa{
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        
        double cateto1, cateto2, hipotenusa;
        
        System.out.println("ingresa el valor del cateto 1:");
        cateto1 = scanner . nextDouble();
        
        System.out.println("Ingrese el valor del cateto 2:");
        cateto2 = scanner .nextDouble();
        
        hipotenusa = Math.sqrt(Math.pow(cateto1 , 2) + Math.pow(cateto2, 2));
        
        System.out.println("El valor de la hipotenusa es " + hipotenusa);
    }
}

