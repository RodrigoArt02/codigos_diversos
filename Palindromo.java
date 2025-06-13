import java.util.Scanner;

public class Palindromo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa una palabra: ");
        String palabra = scanner.nextLine();

        // Convertimos a minúsculas y eliminamos espacios por si acaso
        palabra = palabra.toLowerCase().replaceAll("\\s+", "");

        // Invertimos la palabra
        String palabraInvertida = "";
        for (int i = palabra.length() - 1; i >= 0; i--) {
            palabraInvertida += palabra.charAt(i);
        }

        // Verificamos si es palíndromo
        if (palabra.equals(palabraInvertida)) {
            System.out.println("La palabra es un palíndromo.");
        } else {
            System.out.println("La palabra NO es un palíndromo.");
        }

        scanner.close();
    }
}