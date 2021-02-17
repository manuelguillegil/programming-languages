package main

import "fmt"

func main() {
   var n int
   fmt.Print("Ingrese el número n para calcular su factorial: ")
   fmt.Scanln(&n)
   fmt.Println("Factorial de n: ", factorial(n))
}

// Función que calcula un factorial para un n
func factorial(n int) int {
   if n == 0 {
      return 1
   }

   return n * factorial(n-1)
}