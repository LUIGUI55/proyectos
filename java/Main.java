class MiExcepcion extends Exception {
    public MiExcepcion(String mensaje) {
        super(mensaje);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            lanzarExcepcion();
        } catch (MiExcepcion e) {
            System.out.println("Excepción capturada: " + e.getMessage());
        }
    }

    public static void lanzarExcepcion() throws MiExcepcion {
        throw new MiExcepcion("Esto es una excepción personalizada");
    }
}

