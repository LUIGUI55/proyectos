#include <stdio.h>

float sumar(float a, float b) {
    return a + b;
}

float restar(float a, float b) {
    return a - b;
}

float multiplicar(float a, float b) {
    return a * b;
}

float dividir(float a, float b) {
    if (b != 0)
        return a / b;
    else {
        printf("Error: División entre cero no permitida.\n");
        return 0;
    }
}

int main() {
    int opcion;
    float num1, num2, resultado;

    do {
        printf("\nCalculadora:\n");
        printf("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n");
        printf("Elige una opción: ");
        scanf("%d", &opcion);

        if (opcion >= 1 && opcion <= 4) {
            printf("Introduce el primer número: ");
            scanf("%f", &num1);
            printf("Introduce el segundo número: ");
            scanf("%f", &num2);

            switch (opcion) {
                case 1: resultado = sumar(num1, num2); break;
                case 2: resultado = restar(num1, num2); break;
                case 3: resultado = multiplicar(num1, num2); break;
                case 4: resultado = dividir(num1, num2); break;
            }

            printf("El resultado es: %.2f\n", resultado);
        } else if (opcion != 5) {
            printf("Opción no válida.\n");
        }
    } while (opcion != 5);

    printf("Saliendo de la calculadora.\n");
    return 0;
}


