class Singleton {
    private static Singleton instancia;

    private Singleton() {}

    public static Singleton getInstancia() {
        if (instancia == null) {
            instancia = new Singleton();
        }
        return instancia;
    }
}

public class singleton {
    public static void main(String[] args) {
        Singleton obj1 = Singleton.getInstancia();
        Singleton obj2 = Singleton.getInstancia();
        System.out.println(obj1 == obj2); // true
    }
}
