class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.rear = None

  def enqueue(self, data) -> None:
    # Write your code here
    if self.rear == None:
      self.rear =Node(data)
      self.rear.next=None
      self.rear.data=data
      self.head =self.rear
    else:
      temp = Node(data)
      self.rear.next=temp
      temp.data=data
      temp.next=None
      self.rear=temp
      
  def dequeue(self) -> None:
    # Write your code here
    temp =self.head
    if self.head==None:
      return None
    self.head = temp.next
    if(self.head == None):
      self.rear = None
      
  def status(self) -> None:
    # Write your code here
    temp=self.head
    if (self.head == None and self.rear == None):
      print("None")
    while(temp != None):
      print(temp.data,end="=>")
      temp=temp.next
      if temp==None:
        print("None")

# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
