import BinaryTree
import unittest
from collections import Counter

class TestTreeMethods(unittest.TestCase):
   
   # Se evalua si el arbol es una instancia
    def test_treeInstance(self):
        tree = BinaryTree.BinaryTree(32)
        self.assertIsInstance(tree, BinaryTree.BinaryTree)

    # Se quiere almacenar un bloque de memoria
    def test_new_entry(self):
        tree = BinaryTree.BinaryTree(32)
        self.assertTrue(tree.add(2,'Hilo 1'))

    # Que sucede cuando se utiliza la misma etiqueta para nodos diferentes
    def test_existing_name(self):
        tree = BinaryTree.BinaryTree(32)
        tree.add(1, 'Hilo 1')
        self.assertIsNone(tree.add(2,'Hilo 1'))
    
    # Confirma si un bloque ha sido liberado
    def test_free_block(self):
        tree = BinaryTree.BinaryTree(32)
        tree.add(5, 'Hilo 1')
        self.assertIsNone(tree._free('Hilo 1'))

    # Se liberan dos bloques de memoria con diferentes nombres
    def test_erasing_two_blocks(self):
        tree = BinaryTree.BinaryTree(32)
        tree.add(3, 'Hilo 11')
        tree.add(3, 'Hilo 12')
        self.assertIsNone(tree._free('Hilo 12'))
        self.assertIsNone(tree._free('Hilo 11'))

    # Se añade un bloque con un nombre, se elimina y se vuelve a añadir
    def test_add_erasing_and_add_the_same_name_block(self):
        tree = BinaryTree.BinaryTree(32)
        tree.add(3, 'Hilo 1')
        self.assertIsNone(tree._free('Hilo 1'))
        self.assertTrue(tree.add(2,'Hilo 1'))

    # Chequea si los hijos de un bloque ocupado quedan bloqueados
    def test_children_block(self):
        tree = BinaryTree.BinaryTree(32)
        node = tree.add(4, 'Hilo 1')
        self.assertTrue(node.left_children.occupied == -1)
        self.assertTrue(node.right_children.occupied == -1)

if __name__ == '__main__':
    unittest.main()
