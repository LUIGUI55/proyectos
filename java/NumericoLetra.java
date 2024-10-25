import java.util.Scanner;
public  class NumericoLetra{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese una calificacion numerica de 1-20:");
        int calificacion = scanner .nextInt();
        char calificacionLetra;
        
        if(calificacion >=19 && calificacion <=20){
            calificacionLetra =  'A';
        }else if (calificacion >=16 && calificacion <=18){
            calificacionLetra = 'B';
        }else if (calificacion >=13 && calificacion <=15){
            calificacionLetra = 'C';
        }else if(calificacion >=10 && calificacion <=12){
            calificacionLetra = 'D';
        }else{
            calificacionLetra = 'F';
        }
        System.out.println("La calificacion que se obtuvo fue:" + calificacionLetra);
    }
}

