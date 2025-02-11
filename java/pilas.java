import java.util.Stack;

public class pilas {
    public static void main(String[] args) {
        Stack<Integer> pila = new Stack<>();
        pila.push(10);
        pila.push(20);
        pila.push(30);

        while (!pila.isEmpty()) {
            System.out.println(pila.pop());
        }
    }
}

