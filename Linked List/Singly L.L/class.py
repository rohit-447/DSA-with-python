#create a Linked List Class
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

#class for Linked List
class Linkedlist:
    def __init__(self):
        self.head=None

#insert node at head
    def insert_head(self,value=None):
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode

#print the Linked List
    def print_ll(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

#check list is empty or not
    def is_empty(self):
        if self.head==None:
            print("Empty")
        else:
            print("not empty")

#insert at start
    def insert_at_start(self,value=None):
        self.value=value
        current_node=self.head
        ll.insert_head(value)

#insert at end
    def insert_at_end(self,value=None):
        self.value=value
        current_node=self.head
        new_node=Node(value)
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
    
#search the value in the linked List
    def seach_by_value(self,value=None):
        self.value=value
        current_node=self.head
        while current_node.next:
            if current_node.next==value:
                print("value exists")
                break
            else:
                print("value not exists")
                break

#insert a value after a previous value
    def insert_after(self,prev_value,value)-> None:
        self.pre_value=prev_value
        self.value=value
        current_node=self.head
        while current_node:
            if current_node.data==prev_value:
                new_node=Node(value)
                new_node.next=current_node.next
                current_node.next=new_node
                return
            current_node=current_node.next
    
#delete the first node
    def delete_first(self):
        if self.head is None:
            return
        self.head=self.head.next

#delete last node
    def delete_last(self):
        if self.head is None:
            return
        current_node=self.head
        while current_node.next.next:
            current_node=current_node.next
        current_node.next=None
    
#delete node of certain value
    def delete_item(self,value) -> None:
        self.value=value
        if self.head is None:
                return
        current_node=self.head
        while current_node:
            if current_node.next.data==value:
                current_node.next=current_node.next.next
                return
            current_node=current_node.next
            

#class object variable
ll=Linkedlist()