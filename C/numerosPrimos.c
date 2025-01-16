#include <stdio.h>

int main() {
    int numero, esPrimo = 1;

    printf("Introduce un número: ");
    scanf("%d", &numero);

    if (numero <= 1) {
        esPrimo = 0;
    } else {
        for (int i = 2; i <= numero / 2; i++) {
            if (numero % i == 0) {
                esPrimo = 0;
                break;
            }
        }
    }

    if (esPrimo) {
        printf("%d es un número primo.\n", numero);
    } else {
        printf("%d no es un número primo.\n", numero);
    }

    return 0;
}