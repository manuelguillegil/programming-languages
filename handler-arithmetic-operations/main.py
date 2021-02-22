### MANUEL GUILLERMO GIL 14-10397 14-10397@usb.ve
import sys
from Tree import *

## Funcion que escoge que acción realizar, si es para obtener un árbol o evaluarlo
## @param exp - expresión
## @param isGet - Indica si queremos obtener el árbol o no
## @param isPre - Indica si consideramos PRE o POST
def toAction(exp, isGet = False, isPre = False):
    if(isGet):
        if(isPre):
            return getTree(exp[::-1], True)
        else:
            return getTree(exp, False)
    else:
        if(isPre):
            return eval(exp[::-1])
        else:
            return eval(exp)


## Funcion para obtener el arbol de expresiones
## @param exp - expresion completa
## @param swap - nos indica si es post o pre
def getTree(exp, swap = False):
    stack = []
    if not exp:
        return Tree("")
    for z in exp:
        if (z == ' '):
            continue
        elif (z == '+' or z == '-' or z == '*' or z == '/'):
            if stack:
                x = stack.pop()
            if stack:
                y = stack.pop()
            if swap:
                stack.append(Tree(z,x,y))
            else:
                stack.append(Tree(z,y,x))
        else:  
            stack.append(Tree(z))

    if not stack:
        return Tree("")
    tree = stack.pop()
    return tree

## Funcion para evaluar la expresion
## @param exp - expresion completa
def eval(exp):
    stack = []
    value = 0
    for c in exp:
        if (c == ' '):
            continue
        elif (c=='+' or c=='-' or c=='*' or c=='/'):
            a = stack.pop()
            b = stack.pop()
            if(c == '+'):
                value = int(b) + int(a)
            elif(c == '*'):
                value = int(b) * int(a)
            elif(c == '-'):
                value = int(b) - int(a)
            elif(c == '/'):
                value = int(b) // int(a)
            stack.append(value)
        else:  
            stack.append(c)
    value = stack.pop()
    return value

## Función principal del programa
def main():
    print("------- BIENVENIDO AL MANEJADOR DE OPERACIONES ARTIMETICAS ----")
    option = [""]
    while(True):
        print("--------- Acciones posibles: ----------\n")
        print("SALIR - Salir del programa\n")
        print("MOSTRAR PRE/POST EXPRESION\n")
        print("EVAL PRE/POST EXPRESION\n")
        option = sys.stdin.readline()[:-1].split(' ')        
        if option[0].upper() == "SALIR":
            break

        if(option[1].upper() == "PRE"):
            tree = toAction(option[2:], True, True)
        else:
            tree = toAction(option[2:], True, False)
        if(option[0].upper() == "EVAL" and option[1].upper() == "PRE"):
            print(toAction(option[2:], False, True))
        elif(option[0].upper() == "EVAL" and option[1].upper() == "POST"):
            print(toAction(option[2:], False, False))
        else:
            tree.show()

if __name__ == "__main__":
    main()