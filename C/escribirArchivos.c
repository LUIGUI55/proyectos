#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *archivo;
    char texto[100];

    // Escritura en el archivo
    archivo = fopen("datos.txt", "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    printf("Escribe algo para guardar en el archivo: ");
    scanf(" %[^\n]", texto);
    fprintf(archivo, "%s\n", texto);
    fclose(archivo);
    printf("Datos guardados en 'datos.txt'.\n");

    // Lectura desde el archivo
    archivo = fopen("datos.txt", "r");
    if (archivo == NULL) {
        printf("Error al leer el archivo.\n");
        return 1;
    }

    printf("Leyendo del archivo:\n");
    while (fgets(texto, 100, archivo) != NULL) {
        printf("%s", texto);
    }
    fclose(archivo);

    return 0;
}
