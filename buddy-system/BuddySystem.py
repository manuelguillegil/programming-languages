### MANUEL GUILLERMO GIL 14-10397 14-10397@usb.ve
import BinaryTree

## Funcion principal del Buddy System
## Contiene un menu para elegir que acciones ejecutar
## 1- Reservar espacio en memoria
## 2- Liberar espacio en memoria
## 3- Mostrar el estado actual de la memoria
## 4- Salir del programa
def main():
    print("-------- BUDDY SYSTEM --------")
    while True:
        try:
            blocks = int(input("Introducir el numero de bloques a manejar: "))
            if(blocks >= 1):
                break
            print("La cantidad minima debe ser 1 \n")
        except:
            print("El numero debe ser un entero \n")

    tree = BinaryTree.BinaryTree(2 ** blocks)

    while True:
        print("---- MENU ---- \n")
        print("RESERVAR - Reservar espacio en memoria")
        print("LIBERAR - Liberar espacio en memoria")
        print("MOSTRAR - Mostrar el estado actual de la memoria")
        option = input("SALIR - Finalizar el programa \n\n")
        
        if option.lower() == 'reservar':
            try:
                num_blocks = int(input("Introduzca el numero de bloques a reservar: "))
            except:
                print("Numero de bloques inválido.")
            label = input("Introduzca la label del programa a reservar la memoria: ")
            tree.add(num_blocks, label)
        elif option.lower() == 'liberar':
            label = input("Introduzca la label del programa a liberar los bloques de memoria: ")
            tree._free(label)
        elif option.lower() == 'mostrar':
            tree.print(tree.root)
        elif option.lower() == 'salir':
            break
        else:
            print("Introduzca una opción valida")
            

if __name__ == '__main__':
    main()


