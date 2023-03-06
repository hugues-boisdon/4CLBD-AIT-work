"""
Exercice 2 : Implementation of Circular Linked List and the Josephus Problem

Author: Hugues Boisdon

"""


class Node:

    data = None
    pointer = None

    def __init__(self, _data):
        self.data = _data
    
    def setPointer(self, _node):
        self.pointer = _node
        return self.pointer

    def next(self):
        return self.pointer
    
    def __str__(self):
        return f"{self.data}"


class CircularLinkedList :

    tail = None
    size = 0

    def isEmpty(self):
        return self.size == 0
    

    def head(self):
        return self.tail.next()
    

    def __str__(self):
        ret = "["

        if not self.isEmpty() :

            currentNode = self.head()
            ret += f"{currentNode.data}"

            for i in range(1,self.size):
                currentNode = currentNode.next()
                ret += f", {currentNode.data}"
        
        return ret + "]"


    def find(self, k):
        currentNode = self.head()
        for i in range(k):
            currentNode = currentNode.next()
        return currentNode
    
    

    def insert(self, _data, k):
        inserted = False

        if k == self.size:
            inserted = True
            if self.isEmpty():
                self.tail = Node(_data)
                self.tail.setPointer(self.tail)
            else :
                nodeBefore = self.find(k-1)
                nodeAfter = self.head()
                self.tail = Node(_data)

                nodeBefore.setPointer(self.tail)
                self.tail.setPointer(nodeAfter)
        
        elif not self.isEmpty() and k == 0:
            inserted = True
            nodeBefore = self.tail
            nodeAfter = self.head()
            newNode = Node(_data)

            nodeBefore.setPointer(newNode)
            newNode.setPointer(nodeAfter)
        
        elif not self.isEmpty() and k > -1  and k < self.size :
            inserted = True
            nodeBefore = self.find(k-1)
            nodeAfter  = nodeBefore.next()
            newNode = Node(_data)

            nodeBefore.setPointer(newNode)
            newNode.setPointer(nodeAfter) 

        
        if inserted:
            self.size += 1
        else:
            print(f"Erreur : impossible d'insérer {_data} à l'indice {k}")


    def append(self, _data):
        if not isinstance(_data,list):
            _data = [_data]
        
        for data in _data:
                self.insert(data, self.size)


    def delete(self, k):
        deleted = False
        ret = None

        if not self.isEmpty():
            deleted = True

            if self.size == 1 :
                ret = self.tail.data
                self.tail = None

            else :
                nodeBefore = self.find(k-1)
                ghostNode = nodeBefore.next()
                nodeAfter = ghostNode.next()

                ret = ghostNode.data
                nodeBefore.setPointer(nodeAfter)

                if k == self.size - 1 :
                    self.tail = nodeBefore
        
        if deleted :
            self.size -= 1
        else :
            print(f"Erreur : impossible de supprimer à l'indice {k}")

        return ret


def Josephus(n :int, k :int) -> list:
    """ Implementation of the Josephus problem with circular linked list

    n :       Number of soldiers
    k :       One in k soldiers will be killed
    return :  List of the soldiers killed in order
    """
    permutation = []
    survivors = CircularLinkedList()
    survivors.append([i for i in range(1,n+1)])
    currentSoldier = survivors.head()

    count = 1
    end = False
    while not end:
        nextSoldier = currentSoldier.next()

        if not (currentSoldier.data in permutation):
            if count == k:
                permutation.append(currentSoldier.data)
                count = 1
            else:
                count += 1

        currentSoldier = nextSoldier
        if len(permutation) == n:
            end = True

    return permutation
    

















if __name__ == "__main__":
    print("")
    
    Josephus(41,3)

    print("")