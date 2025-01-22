#include <stdio.h>

int main() {
    int numero, invertido = 0;

    printf("Introduce un número: ");
    scanf("%d", &numero);

    while (numero != 0) {
        int digito = numero % 10;
        invertido = invertido * 10 + digito;
        numero /= 10;
    }

    printf("El número invertido es: %d\n", invertido);

    return 0;
}

