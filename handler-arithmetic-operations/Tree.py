
## Clase que representa el árbol de expresiones
class Tree: 
    ## Función constructor de la clase
    ## @param expr - Expresión
    ## @param right - Hijo derecho
    ## @param left - Hijo izquierdo
    def __init__(self, expr, left = None, right = None):
        self.expr = expr
        self.left  = left
        self.right = right

    # Funcion que hace un recorrido por el arbol para imprimir la expresion en InOrder
    def show(self, endl=1):
        div = self.expr == '/'
        sub = self.expr == '-'
        op = (self.expr == '*' or div) or self.expr == '+' or sub

        if self.left != None:
            if (self.expr == '*' or div) and (self.left.expr == '+' or self.left.expr == '-'):
                print("(", end="") 
            self.left.show(0)
            
            if (self.expr == '*' or div) and (self.left.expr == '+' or self.left.expr == '-'):
                print(")", end="")
        if op:
            print(" ", end="")
        print (str(self.expr),end="")
        if op:
            print(" ", end="")
        if self.right != None:
            if ((self.expr == '*' or div) and (self.right.expr == '+' or self.right.expr == '-')) or (sub and (self.right.expr == '+' or self.right.expr == '-')) or (div and self.right.expr == '*' or self.right.expr == '/'):
                print("(", end="")
            self.right.show(0)
            if ((self.expr == '*' or div) and (self.right.expr == '+' or self.right.expr == '-')) or (sub and (self.right.expr == '+' or self.right.expr == '-')) or (div and self.right.expr == '*' or self.right.expr == '/'):
                print(")", end="")
        if(endl):
            print()