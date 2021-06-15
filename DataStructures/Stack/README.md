# Stacks

## Initialize a stack

```python
from structlinks.structures import Stack

# initialize empty stack
stack = Stack()

# initialize stack with a list
stack_with_list = Stack([1, 2, 3, 4, 5])


print(stack_with_list)
# Output:

# |          5         |
# |          4         |
# |          3         |
# |          2         |
# |          1         |
# |____________________|

```

## Push Elements

```python
from structlinks.structures import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         |
# |          1         |
# |____________________|

stack.push(3)

print(stack)
# Output:

# |          3         |
# |          2         |
# |          1         |
# |____________________|
```

## Push multiple Elements

```python
from structlinks.structures import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         |
# |          1         |
# |____________________|

stack.push_multiple([3, 4, 5])

print(stack)
# Output:

# |          5         |
# |          4         |
# |          3         |
# |          2         |
# |          1         |
# |____________________|
```

## Pop Elements

```python
from structlinks.structures import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         |
# |          1         |
# |____________________|

stack.pop()

print(stack)
# Output:

# |          1         |
# |____________________|
```

## Extend and Add Stacks

```python
from structlinks.structures import Stack

stack1 = Stack([1, 2])
stack2 = Stack([3, 4])

# adding two stacks
stack3 = stack1 + stack2

print(stack3)
# Output:

# |          4         |
# |          3         |
# |          2         |
# |          1         |
# |____________________|

# extend stack1
stack1.extend(stack2)

print(stack1)
# Output:

# |          4         |
# |          3         |
# |          2         |
# |          1         |
# |____________________|
```

## Map Stack to a function

```python
from structlinks.structures import Stack

stack = Stack([1, 2])

print(stack)
# Output:

# |          2         |
# |          1         |
# |____________________|

# map to f(x) = x^2
mapped = stack.map(lambda x: x ** 2)

print(mapped)
# Output:

# |          4         |
# |          1         |
# |____________________|

print(stack)  # <---- stack did not get mutated
# Output:

# |          2         |
# |          1         |
# |____________________|
```

## Invert a Stack

```python
from structlinks.structures import Stack

stack = Stack([1, 2, 3])

print(stack)
# Output:

# |          3         |
# |          2         |
# |          1         |
# |____________________|

stack.invert()

print(stack)
# Output:

# |          1         |
# |          2         |
# |          3         |
# |____________________|
```
