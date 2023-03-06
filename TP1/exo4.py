"""
Exercice 4 : Implementation of HashTables

Author: Hugues Boisdon

"""
from hashlib import sha256
from exo2    import Node, LinkedList
import re
import copy

class RecordEntry:

    key   : str
    value : int

    def __init__(self, _key : str, _value : int):

        self.key   = _key
        self.value = _value



class HashTable_ASCII:

    SIZE = 9495
    entries : list

    def __init__(self):
        (blankEntry := LinkedList()).append(None)
        self.entries = [copy.deepcopy(blankEntry) for i in range(self.SIZE)]

    
    def hash_ASCII(self, key : str) -> int:
        while len(key) < 2:
            key += " "

        offset = int(str(ord(" ")))

        first   = int(str(ord(key[0]))) - offset
        second  = int(str(ord(key[1]))) - offset

        return int(f"{first}{second}")
    
    
    def add(self, _key : str, _value : int):

        index = self.hash_ASCII(_key)
        nodeList : LinkedList = self.entries[index]

        currentNode : Node = nodeList.head
        done = False
        while not done:
            entry : RecordEntry = currentNode.data

            if entry == None:
                done = True
                currentNode.data = RecordEntry(_key, _value)
            elif entry.key == _key:
                done = True
                print("key already exist")
            elif currentNode.nextNode == None:
                done = True
                nodeList.append(RecordEntry(_key, _value))
            currentNode = currentNode.nextNode
        

    def get(self, _key : str) -> int:
        ret = 0
        index = self.hash_ASCII(_key)
        nodeList : LinkedList = self.entries[index]

        currentNode : Node = nodeList.head
        done = False
        while not done:
            entry : RecordEntry = currentNode.data

            if entry == None:
                done = True
                print("invalid key")
                ret = -1
            elif entry.key == _key:
                done = True
                ret = entry.value
            elif currentNode.nextNode == None:
                print("invalid key")
                ret = -1
            currentNode = currentNode.nextNode
        
        return ret
    

    def update(self, _key : str, _value : int):
        index = self.hash_ASCII(_key)
        nodeList : LinkedList = self.entries[index]

        currentNode : Node = nodeList.head
        done = False
        while not done:
            entry : RecordEntry = currentNode.data

            if entry == None:
                done = True
                print("invalid key")
            elif entry.key == _key:
                done = True
                currentNode.data.value = _value
            elif currentNode.nextNode == None:
                done = True
                print("invalid key")
            currentNode = currentNode.nextNode

    
    def delete(self, _key : str):
        index = self.hash_ASCII(_key)
        nodeList : LinkedList = self.entries[index]

        currentNode : Node = nodeList.head
        index = 0
        done = False
        while not done:
            entry : RecordEntry = currentNode.data

            if entry == None:
                done = True
                print("invalid key")
            elif entry.key == _key:
                done = True
                nodeList.delete(index)
            elif currentNode.nextNode == None:
                done = True
                print("invalid key")
            currentNode = currentNode.nextNode
            index += 1
    
    def exist(self, _key : str):
        ret = False
        index = self.hash_ASCII(_key)
        nodeList : LinkedList = self.entries[index]

        currentNode : Node = nodeList.head
        done = False
        while not done:
            entry : RecordEntry = currentNode.data

            if entry == None:
                done = True
            elif entry.key == _key:
                done = True
                ret = True
            elif currentNode.nextNode == None:
                done = True
            currentNode = currentNode.nextNode
        
        return ret
        

class WordOccurences :

    occurences : HashTable_ASCII

    def __init__(self):
        self.occurences = HashTable_ASCII()
    
    def cut(self, text : str):
        cleaned = []
        delimiters = [" ",",",".",";",":","!","?","(",")","[","]","{","}","<",">","-"]
        sub = ""

        for c in text:
            if c in delimiters:
                if (cleanSub := sub.strip()) != "" :
                    cleaned.append(cleanSub)
                sub = ""
            else :
                sub += c
        if (cleanSub := sub.strip()) != "" :
            cleaned.append(cleanSub)

        return cleaned


    def fromString(self, text : str):
        words = self.cut(text)

        for word in words:
            if self.occurences.exist(word) :
                newCount = self.occurences.get(word) + 1
                self.occurences.update(word, newCount)
            else:
                self.occurences.add(word,1)
    
    def fromFile(self, filepath =str):
        file = open(filepath)
        text = file.read()
        file.close()
        return self.fromString(text)
    

    def count(self, word : str):
        ret = 0
        if self.occurences.exist(word):
            ret = self.occurences.get(word)
        return ret


    def __str__(self):
        ret = ""
        for nodeList in self.occurences.entries :
            currentNode : Node = nodeList.head
            done = False
            while not done:
                entry : RecordEntry = currentNode.data
                if entry == None:
                    done = True
                else :
                    ret +=f"\n{entry.key}"+ " "*(15 -len(entry.key)) + "."*len(entry.key)
                    if currentNode.nextNode == None:
                        done = True
                currentNode = currentNode.nextNode
            
        return ret
            

        
                

        
        







if __name__ == '__main__' :
    print("")

    FILEPATH = "TP1\exo4.txt"

    wo = WordOccurences()
    wo.fromFile(FILEPATH)
    print(str(wo))

    print("")

    


