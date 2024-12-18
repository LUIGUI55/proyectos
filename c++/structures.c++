#include <iostream>
using namespace std;

struct Persona {
    string nombre;
    int edad;
};

int main() {
    Persona p = {"Juan", 25};
    cout << "Nombre: " << p.nombre << ", Edad: " << p.edad << endl;
    return 0;
}

