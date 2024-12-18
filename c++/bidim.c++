#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];

    cout << "Introduce los elementos de una matriz 3x3:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> matriz[i][j];
        }
    }

    cout << "Matriz ingresada:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

