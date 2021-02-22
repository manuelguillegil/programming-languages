import Node
import math
## Binary Tree es la clase para el árbol binario, en el cual se encuentra la estructura del Buddy System para el manejo de
## bloques de memoria mediante sus nodos
## @param root - Indica el nodo principal raíz
## @param names - Es una lista que nos indicará cuáles nodos se encuentran o no ocupados
class BinaryTree:
    ## Función de inicialización
    ## @param capacity - capacidad que corresponde al nodo raíz
    ## @param label - etiqueta que corresponde al nodo raíz
    def __init__(self, capacity, label = None):
        self.root = Node.Node(capacity = capacity, label= label )
        self.names = []  
        self.create(self.root)        
    
    ## Funcion para crear el árbol
    ## @param currentNode - Nodo actual
    ## La funcion crea dos instancias de Nodo para el nodo actual, para el hijo izquierdo como derecho
    ## donde la capacidad de los hijos debe ser la capacidad del padre entre dos
    ## La capacidad del padre o nodo actual no debe ser igual a 2, ya que de lo contrario se consideraría una hoja, 
    ## es decir, el nodo con capacidad mínima en el árbol
    def create(self, currentNode):        
        if(currentNode.capacity != 2):
            currentNode.left_children = Node.Node(capacity = currentNode.capacity // 2, father = currentNode)
            currentNode.right_children = Node.Node(capacity = currentNode.capacity // 2, father = currentNode)
            self.create(currentNode.left_children)
            self.create(currentNode.right_children)

    ## Función que añade para un nodo con una etiqueta personalizada una cantidad de bloques a ocupar
    ## @param occupy - cantidad de bloques de memoria a reservar
    ## @param label - etiqueta que el usuario seleccionó
    def add(self, occupy, label):
        if(occupy > self.root.capacity):
            return print("El bloque es mayor al tamaño de memoria maximo")
        if(label in self.names):
            return print("Nombre de label ya existente en memoria")
        capacity = self.root.capacity 
        inserted = self.insert(capacity = int(math.pow(2, int(math.log(occupy, 2)))) if int(math.pow(2, int(math.log(occupy, 2)))) == occupy else int(math.pow(2, int(math.log(occupy, 2) + 1))), occupy= occupy, label= label, currentNode= self.root, array = [])                  
        inserted.occupied = occupy
        inserted.label = label
        self.names.append(label)
        print("El bloque se ha logrado guardar")
        if(inserted.capacity != 2):
            self.occupy_children(inserted.left_children, label)
            self.occupy_children(inserted.right_children, label)
        return inserted

    ## Función que busca en el árbol un espacio disponible para la cantidad de bloques a querer reservar y lo inserta
    ## @param capacity - capacidad que puede ser almacenado
    ## @param occupy - cantidad de bloques a ocupar
    ## @param label - etiqueta con que se identificó el bloque
    ## @param array - arreglo de nombres
    def insert(self, capacity, occupy, label, currentNode, array):
        if(capacity == 1):
            capacity = capacity + 1   
        if (currentNode.capacity == capacity and not(currentNode.occupied)):
            if(currentNode.capacity != 2 ):
                if not(self.check_children(currentNode)):
                    array.append(currentNode)       
            else:            
                array.append(currentNode)      
        else:       
            if(currentNode.capacity!= 2):
                self.insert(capacity, occupy, label, currentNode.left_children, array)       
                self.insert(capacity, occupy, label, currentNode.right_children, array)
        if(array):
            return array[0]

    ## Función que chequea si los hijos de un nodo en particular se encuentran ocupado o no, de forma recursiva
    ## @param currentNode - Nodo actual
    def check_children(self, currentNode):   
        if(currentNode.capacity != 2):    
            if(currentNode.left_children.occupied or currentNode.right_children.occupied):
                return True                
            else:
               return self.check_children(currentNode.left_children) or self.check_children(currentNode.right_children)               
        else:            
            if(currentNode.occupied):
                return True
               
    ## Cuando un nodo padre se encuentra ocupado, esta función se encarga de bloquear sus nodos hijos
    ## @param currentNode - Nodo actual
    ## @param label - etiqueta del nodo
    def occupy_children(self, currentNode, label):
        currentNode.occupied = -1
        currentNode.label = label
        if currentNode.capacity == 2:
            return 

        self.occupy_children(currentNode.left_children, label)
        self.occupy_children(currentNode.right_children, label)

    def _free(self, label):
        if not(label in self.names):
            return print("Imposible liberar memoria")
        return self.free(label, False, self.root)

    ## Función que libera memoria para un bloque particular, en donde tiene que liberar o desbloquear los nodos hijos
    ## @param label - etiqueta a liberar
    ## @param currentNode - Nodo actual
    def free(self, label, children, currentNode):
        if(not children):
            currentNode.occupied = None
            currentNode.label = None
            if currentNode.capacity == 2:
                return 
            self.free(label, True, currentNode.left_children)
            self.free(label, True, currentNode.right_children)
        else:
            if(currentNode.capacity != 2):
                if( currentNode.label == label):
                    currentNode.label = None
                    currentNode.occupied = None
                    if (label in self.names):
                        self.names.remove(label)
                    if(currentNode != self.root and not(currentNode.father.right_children.occupied or currentNode.father.left_children.occupied)):
                        currentNode.father.label = None
                        currentNode.father.occupied = None
                    self.free(label, True, currentNode.left_children)
                    self.free(label, True, currentNode.right_children)
                    return True
                    
                else:
                    return self.free(label, False, currentNode.left_children) or self.free(label, False, currentNode.right_children)
            else:
                if(currentNode.label == label):
                    print(currentNode.label)
                    if (label in self.names):
                        self.names.remove(label)
                    currentNode.label = None
                    currentNode.occupied = None
                    if(not(currentNode.father.right_children.occupied or currentNode.father.left_children.occupied)):
                        currentNode.father.label = None
                        currentNode.father.occupied = None
                    return True

    ## Función para imprimir o mostrar el árbol completo
    ## @param currentNode - Node
    ## @param nivel - Indica el nivel de separación de donde se encuentra el nodo respecto al nodo raíz
    ## @param direccion - Indica si la dirección donde se encuentra es a la derecha o izquierda
    def print(self, currentNode, nivel = 0, direccion = None):
        if currentNode == self.root:
            print(f"[{currentNode.label if currentNode.label else 'Root'} - {currentNode.capacity if currentNode.capacity else 0} / {currentNode.occupied if currentNode.occupied else 0}]")
            self.root.father = currentNode      
        else:   
            for i in range(nivel):
                print("\t",end="")
            if(currentNode):
                print(f"[{(currentNode.label if currentNode.occupied != -1 else 'NODO BLOQUEADO') if currentNode.label else 'Node'} - {currentNode.capacity if currentNode.capacity else 0} / {(currentNode.occupied if currentNode.occupied != -1 else 0) if currentNode.occupied else 0}]", end="")
            print("\n")

        if(currentNode):
            if (currentNode.capacity != 2):
                self.print(currentNode.left_children, nivel + 1, 'izquierdo')
                self.print(currentNode.right_children, nivel + 1, 'derecho')