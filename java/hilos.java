class Contador {
    private int contador = 0;

    public synchronized void incrementar() {
        contador++;
    }

    public int getContador() {
        return contador;
    }
}

public class hilos {
    public static void main(String[] args) throws InterruptedException {
        Contador contador = new Contador();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementar();
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                contador.incrementar();
            }
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Contador final: " + contador.getContador());
    }
}

