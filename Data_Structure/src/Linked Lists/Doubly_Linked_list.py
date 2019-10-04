# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:54:30 2019

@author: mishr
"""
#doubly Linked List

class Node:
    
    def __init__(self, data=None):
        
        self.data = data
        self.next_node = None
        self.prev_node = None
        
class doubly_linked_list:
    
    def __init__(self): 
        self.head = Node()
        
    def append(self, data):
        
        new_node = Node(data)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        
        current.next_node = new_node
        new_node.prev_node = current
        new_node.next_node = None
        
    def length(self):
        
        current = self.head
        counter = 0
        while current.next_node != None:
            counter += 1
            current = current.next_node
        
        return counter
    
    def delete_at(self, index):
        if index >= self.length():
            print("Index Out Of bounds")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            previous_node = current_node.prev_node
            current_node = current_node.next_node
            
            if current_index == index:
                last_node.next_node = current_node.next_node
                last_node.prev_node = previous_node
                return
            current_index += 1
     
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
    
    def display(self):
        
        node_list = []
        current = self.head
        
        while current.next_node is not None:
            
            current = current.next_node
            node_list.append(current.data)
            
        print(node_list)
    
if __name__ == '__main__':
        
    dll = doubly_linked_list()
    
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(7)
    dll.append(8)
    dll.display()
    dll.delete_at(3)
    dll.display()
    dll.get_value_at(4)
    