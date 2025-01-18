public class hilo {
    public static void main(String[] args) {
        Thread hilo = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Hilo ejecutándose: " + i);
            }
        });
        hilo.start();
    }
}