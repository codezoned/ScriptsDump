# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:13:10 2019

@author: mishr
"""

#Singly Linked List
#Node class 

class Node:
    # Function to initialise the node object 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    # Linked List class contains a Node object
        
class singly_linked_list:
     # Function to initialize head 
    def __init__(self):
        self.head = Node()
        
     # Functio to insert a new node
    def append(self, data):
        
        new_node = Node(data)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = new_node
        
     # Functio to know the length of the linked list
    def length(self):
        
        current = self.head
        count = 0
        while current.next_node != None:
            count += 1
            current = current.next_node
        
        return count
    
     # Functio to get value at a position in the linked list
    def get_value_at(self, index):
        
        if index >= self.length():
            print("Index Out Of bounds")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next_node
            if current_index == index:
                return current_node.data
            current_index += 1
        
         # Functio to delete the node in the linked list
    def delete_at(self, index):
        
        if index >= self.length():
            print("Index Out Of bounds")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next_node
            if current_index == index:
                last_node.next_node = current_node.next_node
                return
            current_index += 1
             
                 # Functio to traverse and show the linked list
    def display(self):
        
        node_list = []
        current = self.head
        while current.next_node != None:
            current = current.next_node
            node_list.append(current.data)
            
        print(node_list)
    
if __name__ == '__main__':
    my_list = singly_linked_list()
    my_list.append(0)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.display()
    my_list.get_value_at(3)
    my_list.delete_at(3)
    my_list.display()
    #can use loop to take inputs
        
        
        
