from datetime import datetime
import time
class Node:
    def __init__(self, name, cust_id, number , timestamp):
        self.name = name
        self.cust_id = cust_id  #outlet id for header node
        self.number = number  #waiting time for header node 
        self.timestamp = timestamp
        self.next = None

class Queue:
    def __init__(self , header):
        self.head = header

    def enqueue(self, name, cust_id, number):
        temp = self.head
        time_now = datetime.now()
       # time.sleep(2)
        timestamp = int(round(time_now.timestamp()))
        new_node = Node(name, cust_id, number , timestamp)
        
        if temp is None:
            temp = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def dequeue(self):
        temp = self.head
        temp = temp.next
        if temp is None:
            print("Queue is empty.")
            return
        (self.head).next = temp.next
        del temp

    def delete(self , cust_id):
        temp = (self.head).next
        temp2 = self.head

        while temp != None:
            if temp.cust_id == cust_id:
                temp2.next = temp.next 
                del temp2 
                return 
            temp2 = temp 
            temp = temp.next
        print("Element not found")
        return


    def display(self):
        # here we need to print self.head.number as waiting time for an element thats enqueued onto the queue
        temp = (self.head).next
        if temp is None:
            print("Queue is empty.")
            return
        
        while temp is not None:
            time_now = datetime.now()
            timestamp = int(round(time_now.timestamp()))
            print(f"Name: {temp.name}, Customer ID: {temp.cust_id}, Number: {temp.number} Timestamp: {temp.timestamp} , Time waiting: {timestamp - temp.timestamp}")
            temp = temp.next
        
       

outlets_index = []
for i in range(100):
	#define 
    newnode = Node(None , i , None , 0)
    outlets_index.append(Queue(newnode))

for i in range(100):	
    print(outlets_index[i])

print()


queue1 = outlets_index[0]

queue1.dequeue()
queue1.display()
print()

queue1.enqueue("rohan" , 1 , 4)
queue1.enqueue("rohan" , 2 , 6)
queue1.enqueue("rohan" , 3 , 1)
queue1.enqueue("rohan" , 4 , 2)

queue1.display()
queue1.delete(3)
print()
queue1.display()
print()
queue1.dequeue()
queue1.dequeue()
print()
queue1.display()
print()
queue1.delete(3)
queue1.delete(4)

queue1.display()

"""
Functions on the LL
enqueue
dequeue
delete based on cust_id
"""

"""
we need a global enqueue function with outlet id as parameter
in this func we need to select outlets_index[i] 
and call enqueue on it

same thing for dequeue

"""

#enqeue(outlet_id , user_id , name , number)
#operate on selected queue object
#same for dequeue and delete 

#functions to get outlet id from client and do required operation
#selects required queue from the array and operates on it
def enqueue(outlet_id , name, user_id , number):
    queue = outlets_index[outlet_id]
    queue.enqueue(name , user_id , number)

def dequeue(outlet_id):
    queue = outlets_index[outlet_id]
    queue.dequeue()

def delete(outlet_id , user_id):
    queue = outlets_index[outlet_id]
    queue.delete(user_id)

def display(outlet_id):
    queue = outlets_index[outlet_id]
    queue.display()



#MAIN testing
while(1):
    print("1. ENQUEUE\n 2. DEQUEUE \n 3. DELETE \n 4. DISPLAY")

    inp = int(input())
    if(inp == 1):
        outlet = int(input("enter outlet to enter: "))
        number = int(input("number of seats: "))
        enqueue(outlet , "rohan" , 1 , number)


    elif(inp==2):
        outlet = int(input("enter outlet to enter: "))
        dequeue(outlet)

    elif(inp==3):
        outlet = int(input("enter outlet to enter: "))
        delete(outlet, 1)

    elif(inp==4):
        outlet = int(input("enter outlet to enter: "))
        display(outlet)
    
    else:
        break