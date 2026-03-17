#include <iostream>
#include <string>

using namespace std;

int main() {
    string password_correcta = "naoya123";
    string intento;
    bool acceso = false; // Una bandera para saber si lo logró

    cout << "--- SISTEMA DE SEGURIDAD KALI (3 INTENTOS) ---" << endl;

    // El bucle: empieza en 1, sigue mientras sea <= 3, suma 1 cada vez
    for (int i = 1; i <= 3; i++) {
        cout << "\nIntento [" << i << "/3] - Introduce la clave: ";
        cin >> intento;

        if (intento == password_correcta) {
            cout << "[+] ACCESO CONCEDIDO. Bienvenido, Daniel." << endl;
            acceso = true;
            break; // Rompemos el bucle porque ya entró
        } else {
            cout << "[-] Clave incorrecta.";
        }
    }

    if (!acceso) {
        cout << "\n\n[!!!] SISTEMA BLOQUEADO. Demasiados intentos fallidos." << endl;
    }

    return 0;
}