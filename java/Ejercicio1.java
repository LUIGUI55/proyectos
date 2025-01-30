import java.time.LocalDate;
import java.time.Period;
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese su anio de nacimiento: ");
        int anioNacimiento = scanner.nextInt();

        // Obtener la fecha actual
        LocalDate fechaActual = LocalDate.now();

        // Obtener la fecha de nacimiento como LocalDate
        LocalDate fechaNacimiento = LocalDate.of(anioNacimiento, 1, 1);

        // Calcular la diferencia en años
        Period periodo = Period.between(fechaNacimiento, fechaActual);

        // Mostramos el resultado
        System.out.println("Tienes " + periodo.getYears() + " anios.");
    }
}
