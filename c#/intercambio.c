#include <stdio.h>

int main() {
    int a, b;

    printf("Introduce el valor de a: ");
    scanf("%d", &a);

    printf("Introduce el valor de b: ");
    scanf("%d", &b);

    printf("Antes del intercambio: a = %d, b = %d\n", a, b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("Después del intercambio: a = %d, b = %d\n", a, b);

    return 0;
}