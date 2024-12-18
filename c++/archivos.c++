#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream archivo("datos.txt");
    archivo << "Hola, archivo." << endl;
    archivo.close();

    ifstream leerArchivo("datos.txt");
    string contenido;
    while (getline(leerArchivo, contenido)) {
        cout << contenido << endl;
    }

    leerArchivo.close();
    return 0;
}

