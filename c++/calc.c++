#include <iostream>
using namespace std;

int main() {
    double num1, num2;
    char operacion;

    cout << "Introduce la operación (ejemplo: 3 + 2): ";
    cin >> num1 >> operacion >> num2;

    switch (operacion) {
        case '+': cout << "Resultado: " << num1 + num2 << endl; break;
        case '-': cout << "Resultado: " << num1 - num2 << endl; break;
        case '*': cout << "Resultado: " << num1 * num2 << endl; break;
        case '/': 
            if (num2 != 0) 
                cout << "Resultado: " << num1 / num2 << endl;
            else 
                cout << "Error: División por cero" << endl;
            break;
        default: cout << "Operación no válida" << endl;
    }

    return 0;
}
