

import sys
from ExpressionTree import *



def getTreeFromSufix(expression, swp = 0):

    stack = []

    if not expression:
        return ExpressionTree("") # Expresion vacia

    for c in expression:
        
        if (c == ' '):
            continue
        
        elif (c=='+' or c=='-' or c=='*' or c=='/'):

            if not stack:
                raise Exception("Expresion mal formada. (faltan operandos)")

            a = stack.pop()


            if not stack:
                raise Exception("Expresion mal formada. (faltan operandos)")

            b = stack.pop()

            if swp:
                stack.append(ExpressionTree(c,a,b))
            else:
                stack.append(ExpressionTree(c,b,a))
        
        
        else:  
            stack.append(ExpressionTree(c))


    if not stack:
        return ExpressionTree("") # Expresion vacia

    tree = stack.pop()

    if stack:
        raise Exception("Expresion mal formada. (sobran operandos)")

    return tree


def getTreeFromPrefix(expression):

    return getTreeFromSufix(expression[::-1], 1)


def verifyActionFormat(action):

    if len(action) == 1 and action[0] == "SALIR":
        return True

    if len(action) < 3:
        return False

    if(action[0] != "EVAL" and action[0] != "MOSTRAR"):
        return False

    if(action[1] != "PRE" and action[1] != "POST"):
        return False

    for c in action[2:]:
        if(not c.isdigit() and c != '+' and c != '-' and c != '/' and c != '*'):
            return False

    return True


def menuLoop():
    
    action = [""]

    while(action[0] != "SALIR"):

        print("Ingrese la siguiente accion:")
        action = sys.stdin.readline()[:-1].split(' ')

        if not verifyActionFormat(action):
            print("Formato invalido")
            continue

        if action[0] == "SALIR":
            break

        tree = None

        if(action[1] == "PRE"):
            tree = getTreeFromPrefix(action[2:])
        else:
            tree = getTreeFromSufix(action[2:])

        if(action[0] == "EVAL"):
            print(tree.evaluate())
        else:
            tree.printInOrder()




if __name__ == "__main__":

    menuLoop() # pragma: no cover