/*
1st-Oct.-2024 
Subject: Paradígmas de Programación
Este es la segudna parte de la prática 3 de programación estructurada. La parte uno
fue implementar en Python lo de la practica 2(pagos,potencias y coordenadas).

Instrucciones: Parte II. 
Implementa la función myAtoi(string s), la cual convierta una cadena en enteros de 32 bits;
    Es decir que el límite es (2^32)- 1
El algoritmo debe considerar las siguientes restricciones:

1) Espacios en blanco: deberán ser ignorados.
2) Signos: determinar el signo checando la presencia del signo - o +.
3) Conversión: leer el número, se deben saltar ceros precedentes hasta 
    llegar a los dígitos o al final de la cadena. Si no se leen dígitos el valor final es 0.
4) Redondeo, si el entero está fuera de rango [-2^31 o 2^31-1], redondear el entero
    para que se quede en el rango. Valores menores que -2^31 se quedarán en -2^31 y 
    valores mayores que 2^31-1 se quedarán en 2^31-1.

Ejemplos:
Input: s = "42"
Output: 42

Input: s = " -042"
Output: -42

Input: s = "1337c0d3"
Output: 1337

Input: s = "0-1"
Output: 0

Input: s = "words and 987"
Output: 0

De mis ideas: 
    1) No necesita usar una estructura de datos;
    2) Cada dígito debe ser ponderado, asi 123, el 1 :/ 1*100=100, 2:/2*10=20,3:/3*1=3
*/

#include <stdio.h>
#include "functionsAtoi.h"

int main(int argc, char *argv[])
{
    // (1)Presentación
    printf("Este código solicitará al usuario que ingrese una cadena de texto de hasta %d caracteres, el cual será analizado para regresar un valor entero.\n\n", CAPACITY);

    // (2) Ingresar el mensaje
    unsigned char mensaje[CAPACITY + 1] = "\0";
    printf("Por favor, ingrese una cadéna de texto de hasta %d caracteres(contando espacios).\n",CAPACITY);
    scanf(" %[^\n]", mensaje); // Leer entrada hasta el salto de línea
    limpiar_buffer(); // Limpiar el búfer de entrada

    printf("La cádena de texto ingresada fue: \"%s\"\n", mensaje);
    
    // (3) Procesar el mensaje e imprimir resultado
    int numero = myAtoi(mensaje);//
    if(numero != INT_MAX || numero != INT_MIN)
        printf("El mensaje convertido a entero es ""%d""\n",numero);
    else
        printf("El mensaje convertido a entero es ""%d"", que es el rango inmediato\n",numero);
    
    return 0;////
}
// Por Said Carbot & Elian, ESCOM-IPN-MEX 1-10-24
