#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class Node:
    def __init__(self,parent,left,right,x):
        self.parent = parent
        self.left = left
        self.right = right
        self.x = x
    
class MeldableHeap:
    def __init__(self):
        self.__root = None
        self.__n = 0
        
    def isEmpty(self):
        return self.__root == None
    
    def makeEmpty(self):
        self.__root = None
        self.__n = 0
        
    def getSize(self):
        return self.__n
    
    def add(self,x):
        u = Node(None,None,None,x)
        self.__root = self.__meld(u,self.__root)
        self.__root.parent = None
        self.__n += 1
        
    def remove(self):
        x = self.__root.x
        self.__root = self.__meld(self.__root.left,self.__root.right)
        if self.__root != None:
            self.__root.parent = None
        self.__n -= 1
        return x
    
    def __meld(self,q1,q2):
        if q1 == None:
            return q2
        if q2 == None:
            return q1
        if q2.x < q1.x:
            return self.__meld(q2,q1)
        if bool(random.getrandbits(1)):
            q1.left = self.__meld(q1.left,q2)
            q1.left.parent = q1
        else:
            q1.right = self.__meld(q1.right,q2)
            q1.right.parent = q1
        return q1
    
    def displayHeap(self):
        print("\nMeldable Heap : ",end="")
        if self.__root == None:
            print("Empty")
            return
        
        prev = self.__root
        w = self.__root
        while w.left != None:
            w = w.left
            
        while w != None:
            print(w.x,end=" ")
            prev = w
            w = self.__nextNode(w)
        print()
    
    def __nextNode(self,w):
        if w.right != None:
            w = w.right
            while w.left != None:
                w = w.left
        else:
            while w.parent != None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
print("Meldable Heap Test\n\n")
mh = MeldableHeap()
while True:
    print("\nMeldable Heap Operations\n");
    print("1. add");
    print("2. remove");
    print("3. size");            
    print("4. check empty");
    print("5. clear");
    choice = int(input("Please Select: "))
    if choice == 1:
        x = int(input("Enter integer element to insert"))
        mh.add(x)
    elif choice == 2:
        print("Removed Element :",mh.remove())
    elif choice == 3:
        print("Size =", mh.getSize())
    elif choice == 4:
        print("Empty status =", mh.isEmpty())
    elif choice == 5:
        mh.makeEmpty()
        print("Heap Cleared\n")
    else:
        print("Wrong Entry \n ")
        
    mh.displayHeap()
    x = input("Do you want to continue (Type y or n)")
    if x == "N" or x == "n":
        break


# In[ ]:





# In[ ]:




