import java.util.Scanner;

class volumen{
    public static void main (String [] args){

        Scanner s = new Scanner(System.in);

        System.out.println("Introduce el radio de la esfera");

        double r=s.nextDouble();

        double volumen = (4*22 *r*r*r)/(3*7);

        System.out.println("Ele volumen es:" + volumen);

        
    }
}