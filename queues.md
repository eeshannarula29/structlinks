---
title: Queues
filename: queues
--- 

# Queues

## Initialize a Normal Queue

```python
from structlinks.structures import Queue

# initialize empty queue
queue = Queue()

# initialize queue with list
queue_with_list = Queue([1, 2, 3])

print(queue)
# Output:
# [1 -> 2 -> 3]
```

## Initialize a Priority Queue

```python
from structlinks.structures import Queue

priority_func = lambda x: len(x)

queue = Queue(['hi', 'hello', 'hey'], metric = priority_func)

print(queue)
# Output:
# [hi -> hey -> hello]
```

## Initialize Queue / Priority Queue with Limit

Add a limit to the queue to limit the number of elements in a queue, This can be done by adding limit
attribute while initializing a queue.

```python
from structlinks.structures import Queue

queue = Queue(['hi', 'hello', 'hey'], limit = 5)
```

## Interchange between Queue and Priority Queue

Queue and Priority Queue are interchangeable and can be converted from one to another

### Queue --> Priority Queue

```python
from structlinks.structures import Queue

# Initialize a queue
queue = Queue(['hi', 'hello', 'hey'])

# define a priority function
priority_func = lambda x: len(x)

# convert Queue to Priority Queue
queue.change_metric(priority_func)
```

### Priority Queue --> Queue

```python
from structlinks.structures import Queue

# define a priority function
priority_func = lambda x: len(x)

# Initialize a Priority Queue
queue = Queue(['hi', 'hello', 'hey'], metric = priority_func)

# convert Priority Queue to Queue
queue.change_metric(None)
```

## Change Limit

```python
from structlinks.structures import Queue

# Initialize a queue with limit
queue = Queue(['hi', 'hello', 'hey'], limit = 3)

queue.change_limit(4)  # <---- changes the limit to 4

queue.change_limit(None)  # <---- removes the limit
```

## Check for Empty / Filled Queue

```python
from structlinks.structures import Queue

# Initialize a queue with limit
queue = Queue(['hi', 'hello', 'hey'], limit = 3)

print(queue.is_filled)
# Output:
# True

print(queue.is_empty)
# Output:
# False
```

## Enqueue / Push Elements

The function used to enqueue/push element from queue, takes constant time. If the limit of the queue has been obtained
the `QueueLimitReachedError` will be raised.

```python
from structlinks.structures import Queue

# Initialize a queue
queue = Queue([100, 200, 300])

print(queue)
# Output:
# [100 -> 200 -> 300]

queue.enqueue(50)  # <--- push 50 into the queue

print(queue)
# Output:
# [50 -> 100 -> 200 -> 300]
```

## Dequeue / Pop Elements

The function used to Dequeue/Pop element, takes constant time. If the queue is empty then
the `EmptyQueueError` will be raised.

```python
from structlinks.structures import Queue

# Initialize a queue
queue = Queue([100, 200, 300])

print(queue)
# Output:
# [100 -> 200 -> 300]

element = queue.dequeue()  # <--- pop element

print(element)
# Output:
# 300

print(queue)
# Output:
# [100 -> 200]
```

## Extend Queue

```python
from structlinks.structures import Queue

q1 = Queue([100, 200, 300])
q2 = Queue([400, 500, 600])

q2.extend(q1)  # <--- Extend q2 by q1

print(q2)
# Output:
# [100 -> 200 -> 300 -> 400 -> 500 -> 600]
```

## Map a Queue

```python
from structlinks.structures import Queue

# Initialize a queue
queue = Queue([1, 2, 3])

# create a mapping function
mapping_function = lambda x: x ** 2

# map the function to queue
queue.map(mapping_function)

print(queue)
# Output:
# [1 -> 4 -> 9]
```

## Printing Custom Queues

Queues can be printed to get specific properties of a elements in the queue.

```python
from structlinks.structures import Queue
from dataclasses import dataclass

@dataclass
class Person:
    name: str

david = Person('David')
mario = Person('Mario')

people_queue = Queue([david, mario])

people_queue.display(lambda person: person.name)
# Output:
# Entry ---------------> Exit
#       David -> Mario
# ---------------------------
```
