from collections import deque


# Function to evaluate a postfix expression
def evaluatePostfix(expression):
    stack = deque()  # Initialize an empty stack to hold operands

    # Traverse each character in the postfix expression
    for char in expression:
        if (char >= '0' and char <= '9'): # char.isdigit() can also be used
            # If the character is an operand, convert to integer and push to stack
            stack.append(int(char))
        else:
            # If the character is an operator, pop top two elements for operation
            op2 = stack.pop()
            op1 = stack.pop()

            # Perform the operation based on the operator
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '/':
                # Use integer division
                stack.append(op1 // op2)
            elif char == '^':
                stack.append(op1 ** op2)

    # Final result will be the only element left in the stack
    return stack[-1]

expression = "231*+9-"
ans = evaluatePostfix(expression)

'''
Time Complexity: O(n)

Space Complexity: O(n)
'''