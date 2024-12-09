#include <stdio.h>

int main() {
    int n;
    float suma = 0;

    printf("¿Cuántos números quieres promediar?: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        float numero;
        printf("Introduce el número %d: ", i);
        scanf("%f", &numero);
        suma += numero;
    }

    printf("El promedio es: %.2f\n", suma / n);

    return 0;
}
