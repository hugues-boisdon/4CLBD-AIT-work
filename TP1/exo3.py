"""
Exercice 3 : Implementation of Stack using Linked List

Author: Hugues Boisdon

"""

from exo2 import Node, LinkedList


class Stack:

    stackList = None

    def __init__(self):
        self.stackList = LinkedList()


    def enqueue(self, _data):
        self.stackList.insert(_data,0)


    def peek(self):
        return self.stackList.head.data
    

    def dequeue(self):
        ret = None
        if(not self.stackList.isEmpty()):
            ret = self.stackList.delete(0)
        return ret
    
    def size(self):
        return self.stackList.size
    
    def isEmpty(self):
        return self.stackList.isEmpty()
    







def syntaxValidator(filePath):

    file = open(filePath)

    openers = ["(", "{", "<", "["]
    enders  = [")", "}", ">", "]"]

    stack = Stack()
    valid = True
    k = 0

    for line in file.readlines():
        if( not valid):
            break
        k += 1

        for char in line :
            if char in openers:
                stack.enqueue(char)

            elif char in enders:
                lastChar = stack.dequeue()
                currentValid = False
                if lastChar in openers:
                    if openers.index(lastChar) == enders.index(char):
                        currentValid = True
                if(not currentValid):
                    valid = False
                    break
    file.close()

    if(valid):
        print("Syntaxe Valide")
    else:
        print("Syntaxe Invalide à la ligne " + str(k))



  









if __name__ == '__main__':    
    print("")

    syntaxValidator("TP1\exo3.txt")

    print("")