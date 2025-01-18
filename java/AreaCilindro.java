import java.util.Scanner;

public class AreaCilindro{
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el radio del cilindro");
        double radio = scanner .nextDouble();
         System.out.print("ingresa la altura del cilindro");
         double altura = scanner .nextDouble();
         double volumen = Math.PI * Math.pow(radio, 2) * altura;
         double area = 2* Math.PI * radio * (altura +radio);
         
         // Mostramos los resulatados
         System.out.println("El volumen del circulo es " + volumen );
         System.out.println("El area del cilindro es:" + area);
    }
}