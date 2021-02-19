// MANUEL GUILLERMO GIL 14-10397 <14-10397@usb.ve>
#include <stdio.h>
#include <string.h>
#include <time.h>
// alpha = 5
// beta = 4
// f5,4(n)

// 5.a
// Función recursiva
// @param int n - número entero a evaluar en la recursión
int recursive_func(int n) {
  if (n < 20) {
    return n;
  };
  return recursive_func(n - 4) + recursive_func(n - 8) + recursive_func(n - 12) + recursive_func(n - 16) + recursive_func(n - 20);
}

// 5.b
// Función recursiva auxiliar que es utilizada por la función recursiva de cola
// @param int f1 - entero como primer argumento que se irá acumulando con la suma de los demás f2...f5
// @param int f2 - entero que se irá desplazando el valor anterior en la recursión
// @param int f3 - entero que se irá desplazando el valor anterior en la recursión
// @param int f4 - entero que se irá desplazando el valor anterior en la recursión
// @param int f5 - entero que se irá desplazando el valor anterior en la recursión
// @param int i - entero que servirá de índice para cada ciclo de la recursión, el cual tendrá un desplazamiento de 4 en 4
// @param int n - entero con el valor que interesa evaluar en la recursión
int tail_recursive_func_aux(int f1, int f2, int f3, int f4, int f5, int i, int n) {
  if (i == n) {
    return (f1 + f2 + f3 + f4 + f5);
  }
  return tail_recursive_func_aux(
    f1 + f2 + f3 + f4 + f5, 
    f1,
    f2,
    f3,
    f4,
    i + 4, 
    n
  );
}

// Función principal de la recursión de cola, el cual utiliza la función de tail_recursive_func_aux para cada ciclo recursivo
// @param n - entero del número que queremos evaluar
int tail_recursive_func(int n) {
  if (n < 20) {
    return n;
  } else {
    int i = 20 + (n % 4);
    return tail_recursive_func_aux(i - 4, i - 8 , i - 12 , i - 16, i - 20, i, n);
  };
}

// 5.c
// Función itertivo de la función recursiva
// @param int n - entero el cual nos interesa evaluar
int iterative_recursive_func(int n) {
  if (n < 20) {
    return n;
  } else {
    int i = 20 + (n % 4);
    int t, f1 = i - 4, f2 = i - 8, f3 = i - 12, f4 = i - 16, f5 = i - 20;
    while (i <= n) {
      t = f1 + f2 + f3 + f4 + f5;
      f5 = f4;
      f4 = f3;
      f3 = f2;
      f2 = f1;
      f1 = t;
      i = i + 4;
    }
    return f1;
  }
}

// Función que contiene nuestro programa principal
int main (void){
  int n = 0;
  printf("Ingrese el valor de un número entero para las diferentes funciones recursivas: \n");
  scanf("%i", &n);

  clock_t t;
  t = clock();
  printf("Función recursiva normal: %i\n", recursive_func(n));
  double time = ((double) t) / CLOCKS_PER_SEC;
  printf("Tiempo: %f\n", time);

  t = clock() -t;
  printf("Función recursiva de cola: %i\n", tail_recursive_func(n));
  time = ((double) t) / CLOCKS_PER_SEC;
  printf("Tiempo: %f\n", time);

  t = clock() -t;
  printf("Función recursiva iterativo: %i\n", iterative_recursive_func(n));
  time = ((double) t) / CLOCKS_PER_SEC;
  printf("Tiempo: %f\n", time);
}