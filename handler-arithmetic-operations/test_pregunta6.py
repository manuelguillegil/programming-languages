#test_tutorial.py
from pregunta6 import *
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import os
import subprocess

tree1 = ExpressionTree(
            "+",
            ExpressionTree("5"),
            ExpressionTree(
                "-",
                ExpressionTree("2"),
                ExpressionTree(
                    "*",
                    ExpressionTree("3"),
                    ExpressionTree(
                        "/",
                        ExpressionTree("4"),
                        ExpressionTree("2")
                    )
                )
            )
        )

tree2 = ExpressionTree(
            "*",
            ExpressionTree(
                "+",
                ExpressionTree("2"),
                ExpressionTree("1")
            ),
            ExpressionTree(
                "-",
                ExpressionTree("6"),
                ExpressionTree("1")
            )
        )

class pregunta6Test(TestCase):


    def test_evaluate_expression_tree(self):

        output = tree1.evaluate()
        expected_output = 1

        self.assertEqual(output, expected_output)


    def test_print_in_order_expression_tree(self):

        expected_output = "(2 + 1) * (6 - 1)"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            tree2.printInOrder()
            self.assertEqual(fake_out.getvalue()[:-1], expected_output)

    def test_verify_action_format(self):

        expression = ['ola', 'jeje', 'jaweno']

        output = verifyActionFormat(expression)

        self.assertFalse(output)

    def test_get_tree_from_prefix(self):

        expression = ['+','0','1']
        expected_output = ExpressionTree(
                            '+',
                            ExpressionTree('0'),
                            ExpressionTree('1')
        )

        output = getTreeFromPrefix(expression)

        self.assertEqual(str(output), str(expected_output))

    def test_menu_loop(self):

        input_ = "EVAL PRE + * + 3 4 5 7\nMOSTRAR POST 8 3 - 8 4 4 + * +\nSALIR\n"
        
        with patch('sys.stdin', StringIO(input_)) as mocked_stdin:
            with patch('sys.stdout', new=StringIO()) as mocked_stdout:

                menuLoop()

                output = mocked_stdout.getvalue()
                expected_output = "Ingrese la siguiente accion:\n42\nIngrese la siguiente accion:\n8 - 3 + 8 * (4 + 4)\nIngrese la siguiente accion:\n"

                self.assertEqual(output, expected_output)