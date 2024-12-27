import java.io.*;

class Persona implements Serializable {
    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{nombre='" + nombre + "'}";
    }
}

public class objetos {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Persona persona = new Persona("Carlos");

        // Serializar
        ObjectOutputStream salida = new ObjectOutputStream(new FileOutputStream("persona.ser"));
        salida.writeObject(persona);
        salida.close();

        // Deserializar
        ObjectInputStream entrada = new ObjectInputStream(new FileInputStream("persona.ser"));
        Persona personaLeida = (Persona) entrada.readObject();
        entrada.close();

        System.out.println(personaLeida);
    }
}
