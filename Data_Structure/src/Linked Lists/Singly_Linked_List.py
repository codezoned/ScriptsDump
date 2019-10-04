# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:13:10 2019

@author: mishr
"""

#Singly Linked List 

class Node:
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    
        
class singly_linked_list:
    def __init__(self):
        
        self.head = Node()
    
    def append(self, data):
        
        new_node = Node(data)
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = new_node
    
    def length(self):
        
        current = self.head
        counter = 0
        while current.next_node != None:
            counter += 1
            current = current.next_node
        
        return counter
    
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
        
        
        