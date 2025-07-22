class listNode():
    def __init__(self,prev,val,next):
        self.prev,self.val,self.next = prev,val,next
        

class MyCircularQueue(object):
    

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.left = listNode(None,0,None)
        self.right = listNode(self.left,0,None)
        self.left.next = self.right
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.newNode = listNode(self.right.prev,value,self.right)
        self.left.next = self.newNode
        self.right.prev = self.newNode
        self.size -= 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
           return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size += 1
        return True

        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return-1
        else:
            return self.left.next.val  
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
             return self.right.prev.val  
        
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.left.next == self.right
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == 0

        

