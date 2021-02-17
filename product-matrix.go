package main

import (
	"fmt"
)

func main() {
	var matrixA [10][10]int 
	var matrixB [10][10]int 
	var result [10][10]int 
	var i, j, k, m, n, p, q, total int 
	total = 0 

	fmt.Print("Ingrese la cantidad de filas de la primera matriz: ") 
	fmt.Scanln(&m) 
	fmt.Print("Ingrese la cantidad de columnas de la segunda matriz: ") 
	fmt.Scanln(&n) 
	fmt.Print("Ingrese la cantidad de filas de la segunda matriz: ") 
	fmt.Scanln(&p) 
	fmt.Print("Ingrese la cantidad de columnas de la segunda matriz: ") 
	fmt.Scanln(&q)

	if n != p { 
		fmt.Println("Las dos matrices no pueden ser multiplicadas") 
		} else { 
			fmt.Println("Ingrese los elementos de la primera matriz: ") 
			for i = 0; i < m; i++ { for j = 0; j < n; j++ { 
				fmt.Scan(&matrixA[i][j]) 
		} 
	}

	fmt.Println("Ingrese los elementos de la segunda matriz: ") 
	for i = 0; i < p; i++ { 
		for j = 0; j < q; j++ { 
		fmt.Scan(&matrixB[i][j]) 
		} 
	} 
	for i = 0; i < m; i++ { 
		for j = 0; j < q; j++ { 
			for k = 0; k < p; k++ { 
				total = total + matrixA[i][k]*matrixB[k][j] 
			} 
			result[i][j] = total 
			total = 0 
		} 
	} 
	fmt.Println("El resultado de multiplicar ambas matrices son: ") 
	for i = 0; i < m; i++ { 
		for j = 0; j < n; j++ { 
			fmt.Print(result[i][j], "\t") } 
		} 
	}
	fmt.Println()
}

