# Problem

Implement Queue using Linked list</b>

To implement a queue using the singly linked list concept, all the singly linked list operations are performed based on Queue operations FIFO(first in first out).</br>
Assume all nodes in the linked list are 0-indexed.


Implement the Queue class:
> **enqueue(data)** : Add data to the queue.</br>
**dequeue()** : Remove data from the queue.</br>
**status()** : Display the elements of queue.</br>

# Constraints
Data should be integer value.

## Sample Input - 1
```
enqueue, enqueue, enqueue, dequeue, dequeue
3, 4, 5, -, -
```
## Sample Output - 1
```
5=>None
```
## Sample Input - 2
```
enqueue, enqueue, enqueue
1, 2, 3
```
## Sample Output - 2
```
1=>2=>3=>None
```
## Sample Input - 3
```
enqueue, enqueue, enqueue, dequeue, dequeue, enqueue, enqueue
1, 2, 3, -, -, 2, 3
```
## Sample Output - 3
```
3=>2=>3=>None
```
