#include <stdio.h>

int main() {
    int numero;

    printf("Introduce un número para su tabla de multiplicar: ");
    scanf("%d", &numero);

    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }

    return 0;
}
