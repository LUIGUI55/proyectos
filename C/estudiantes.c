#include <stdio.h>
#include <string.h>

struct Estudiante {
    char nombre[50];
    int edad;
    float promedio;
};

int main() {
    int n;

    printf("¿Cuántos estudiantes quieres registrar?: ");
    scanf("%d", &n);

    struct Estudiante estudiantes[n];

    for (int i = 0; i < n; i++) {
        printf("\nEstudiante %d:\n", i + 1);
        printf("Nombre: ");
        scanf(" %[^\n]", estudiantes[i].nombre);
        printf("Edad: ");
        scanf("%d", &estudiantes[i].edad);
        printf("Promedio: ");
        scanf("%f", &estudiantes[i].promedio);
    }

    printf("\nLista de Estudiantes:\n");
    for (int i = 0; i < n; i++) {
        printf("Nombre: %s, Edad: %d, Promedio: %.2f\n",
               estudiantes[i].nombre, estudiantes[i].edad, estudiantes[i].promedio);
    }

    return 0;
}SS