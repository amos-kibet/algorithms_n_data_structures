"""
Implements LIFO operation sequence.
OPerations:
  * Push
  * Pop
  * Peek
"""
class Stack():
  # Initialize a stack as a list
  def __init__(self):
    self.items = []

  # Check if stack is empty
  def is_empty(self):
    return self.items == []

  # Push to stack
  def push(self, item):
   self.items.append(item)

  # Pop operations
  def pop(self):
    return self.items.pop()

  # Peek operation
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    return "Stack is empty!"

  # Get stack items
  def get_stack(self):
    return self.items


# Driver code
my_stack = Stack()
# Peek an empty stack
print(my_stack.peek()) 
# Append two items to stack
my_stack.push("A")
my_stack.push(1)
# Peek stack
print(my_stack.peek()) 
