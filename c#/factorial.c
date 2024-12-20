#include <stdio.h>

int main() {
    int numero, factorial = 1;

    printf("Introduce un número: ");
    scanf("%d", &numero);

    for (int i = 1; i <= numero; i++) {
        factorial *= i;
    }

    printf("El factorial de %d es %d\n", numero, factorial);

    return 0;
}


