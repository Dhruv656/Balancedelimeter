# Balancedelimeter
This code checks if the brackets in an arithmetic expression are balanced or not using a stack-based approach. If the brackets are not balanced, it returns False, otherwise it returns True.



The code implements a stack-based approach to checking whether the brackets in an arithmetic expression are balanced or not. It defines two classes, bnode and MyStack. The bnode class represents a single bracket and has a showInfo method that prints out the type of bracket. The MyStack class is a stack implementation that uses bnode objects to store the brackets. It has methods to push a new bracket onto the stack, pop the top bracket from the stack, and check if the stack is empty.

The BraceStacks function prompts the user to enter an arithmetic expression, then iterates through each character in the expression. If the character is an opening bracket ({, [, or (), it creates a new bnode object representing that bracket and pushes it onto the stack. If the character is a closing bracket (}, ], or )), it pops the top bracket from the stack and checks if it matches the closing bracket. If the brackets do not match, the function returns False, indicating that the brackets are not balanced. If the stack is empty at the end of the iteration, the function returns True, indicating that the brackets are balanced. Otherwise, it returns False.

Finally, the main code block calls the BraceStacks function and prints either "Balanced" or "Imbalanced" depending on the result.
