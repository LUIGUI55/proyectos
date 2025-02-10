import java.io.*;

public class  linea {
    public static void main(String[] args) {
        try (BufferedReader lector = new BufferedReader(new FileReader("archivo.txt"))) {
            String linea;
            while ((linea = lector.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}