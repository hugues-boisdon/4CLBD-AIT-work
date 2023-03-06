"""
Exercice 2 : Implementation of Linked List

Author: Hugues Boisdon

"""



class Node:

    data = None
    nextNode = None

    def __init__(self, _data):
        self.data = _data



class LinkedList:

    head = None
    size = 0

    def getPreviousNode(self,k):
        previousNode = self.head
        if (k > 0):
            for i in range(k-1):
                previousNode = previousNode.nextNode
        return previousNode


    def isEmpty(self):
        return self.head == None




    def insert(self, _data, k):
        self.size += 1

        if(self.isEmpty() and k == 0):
            self.head = Node(_data)

        elif(k == 0):
            nextNode = self.head
            self.head = Node(_data)
            (self.head).nextNode = nextNode

        elif k <= self.size - 1:
            previousNode = self.getPreviousNode(k)

            nextNode = previousNode.nextNode

            previousNode.nextNode = Node(_data)
            (previousNode.nextNode).nextNode = nextNode
        else:
            self.size -= 1
            print("Erreur: indice trop grand")
    

    def append(self, _data):
        if isinstance(_data,list):
            appends = _data
        else:
            appends = [_data]

        for subData in appends:
                if(self.isEmpty()):
                    self.insert(subData, 0)
                else:
                    self.insert(subData, self.size)


    def delete(self, k):
        ret = None

        if( not self.isEmpty()):
            self.size -= 1

            if(k == 0):
                ret = self.head.data
                self.head = (self.head).nextNode
            else :
                previousNode = self.getPreviousNode(k)

                nextNode = (previousNode.nextNode).nextNode
                ret = (previousNode.nextNode).data

                previousNode.nextNode = nextNode
        return ret
    


    def find(self, _data):
        i = -1

        if( not self.isEmpty()):
            currentNode = self.head
            i = 0

            if (currentNode.data != _data):
                while (currentNode.data != _data):
                    if(currentNode.nextNode == None):
                        i = -1
                        break
                    currentNode = currentNode.nextNode
                    i += 1
        return i



    def __str__(self):
        ret = "["
        if(not self.isEmpty()):
            currentNode = self.head
            ret += str(currentNode.data)
            while(currentNode.nextNode != None):
                currentNode = currentNode.nextNode
                ret += ", " + str(currentNode.data)
        ret += "]"
        return ret


# Tests
if __name__ == '__main__':    
    print("")


    l = LinkedList()

    l.append(5)
    print(l)

    l.append("oui")
    print(l)

    l.append("yaya")
    print(l)

    l.insert("non", 15)
    print(l)

    print("")








