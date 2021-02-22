### Clase Node que corresponde a un nodo particular del árbol
## @param capacitiy - Indica la capacidad que posee de almacenamiento
## @param occupied - Indica si el nodo se encuentra ocupado o no
## @param label - Es la etiqueta para diferenciar al nodo del resto
## @param left - Es el hijo que se encuentra a la izquierda
## @param right - Es el hijo que se encuentra a la derecha
## @param father - Indica al nodo padre (o a la raíz)
class Node:
    def __init__(self, capacity , occupied = None, label = None, left = None, right = None, father = None):
        self.capacity = capacity
        self.occupied = occupied
        self.label = label
        self.left_children = left
        self.right_children = right
        self.father = father