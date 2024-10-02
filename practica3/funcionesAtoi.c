/*
1-oct-2024
Compendio de las funciones creadas
*/
#include <stdio.h>
#include <ctype.h>
#include <limits.h>
#include "functionsAtoi.h"

/* A Functions
INDICE
A.1) myAtoi
A.2) Quitar espacios
A.3) limpiar_buffer
*/

//A.1) My Atoi
int myAtoi(unsigned char *cadena)
{
    eliminarEspacios(cadena);       //A.2
    int resultado = 0;
    int signo = 1;
    if(*cadena == '-')
    {
        signo = -1;
        cadena++;
    }
    while (*cadena && isdigit(*cadena))//recorro mientras halla algo en la cadena y sea digito
        {
            // resto para obtener el valor unitario base 10
            // Y tambien ponderar
            int digito = *cadena - '0';

            resultado = resultado * 10 + (*cadena - '0');
            if (signo == 1 && resultado > (INT_MAX - digito) / 10)
            {
                printf("Número fuera de rango, se redondea a (2^31)-1\n");
                return INT_MAX;
            }
            else if (signo == -1 && -resultado <  (INT_MIN + digito) / 10)
            {
                printf("Número fuera de rango, se redondea a -[(2^31)-1]\n");
                return INT_MIN;
            }
            cadena++;
        }
    return resultado * signo;
}

// A.2) Elminar Espacios
void eliminarEspacios(unsigned char *cadena)
{
    unsigned char *inicio = cadena;
    unsigned char *sinEspacios = cadena;
    while (*cadena)
    {
        if (*cadena != ' ')
        {
            *sinEspacios = *cadena; // Copiar caracteres diferentes a espacios
            sinEspacios++;
        }
        cadena++;
    }
    *sinEspacios = '\0'; // Agregar el carácter nulo al final de la cadena sin espacios
    //printf("La cadena sin espacios es: \"%s\"\n", inicio);
}
// A.3 Limpiar el buffer
void limpiar_buffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
    {
        // Vaciar el búfer de entrada
    }
}
