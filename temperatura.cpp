#include <iostream>
using namespace std;

int main() {
    double celsius;

    // Pedimos al usuario la temperatura en Celsius
    cout << "Ingresa la temperatura en grados Celsius: ";
    cin >> celsius;

    // Convertimos a las otras escalas
    double fahrenheit = (celsius * 9.0 / 5.0) + 32;
    double kelvin = celsius + 273.15;
    double rankine = (celsius + 273.15) * 9.0 / 5.0;

    // Mostramos los resultados
    cout << "Fahrenheit: " << fahrenheit << " °F" << endl;
    cout << "Kelvin: " << kelvin << " K" << endl;
    cout << "Rankine: " << rankine << " °R" << endl;

    return 0;
}