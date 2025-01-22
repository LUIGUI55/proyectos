#include <stdio.h>

int main() {
    int matriz[2][2], suma = 0;

    printf("Introduce los valores de la matriz 2x2:\n");

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("Elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
            suma += matriz[i][j];
        }
    }

    printf("La suma de los elementos es: %d\n", suma);

    return 0;
}
